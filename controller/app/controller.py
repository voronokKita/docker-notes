from flask import request, redirect, url_for, flash

from flask_config import FLASK
from models import TestTransactions, NoteTransactions
from forms import AddNewNoteForm
import views


DB = NoteTransactions()
TEST_DB = TestTransactions()


@FLASK.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form = AddNewNoteForm()
        if form.validate_on_submit():
            formdata = form.txt.data
            DB.write_note(formdata)
            flash('A new note added')
            return redirect(url_for('index'), 301)

    data = DB.read_note_list()
    view = views.index(data)
    return view, 200


# Test routes

@FLASK.route('/ping', methods=['GET'])
def ping():
    return 'pong', 200


@FLASK.route('/testdb', methods=['GET'])
@FLASK.route('/testdb-<int:id_>', methods=['GET'])
def test_db(id_=None):
    result = TEST_DB.read_test(row=id_)

    if not result:
        return 'Read successful, nothing was found.'
    elif isinstance(result, list):
        responce = ''
        for row in result:
            responce += f'{row.id} - {row.num}, {row.txt} <br>'
        return responce.removesuffix('<br>')
    else:
        return f'{result.id} - {result.num}, {result.txt}'


@FLASK.route('/testwrte-<int:num>-<string:txt>', methods=['GET'])
def test_write(num, txt):
    TEST_DB.write_test(num, txt[:10])
    return redirect(url_for('test_db'), 302)

