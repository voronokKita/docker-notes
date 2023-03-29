from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class AddNewNoteForm(FlaskForm):
    txt = TextAreaField('Write a new note', validators=[DataRequired()])
