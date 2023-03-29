from flask import render_template

from forms import AddNewNoteForm

def index(data):
    return render_template('index.html', note_list=data, form=AddNewNoteForm())
