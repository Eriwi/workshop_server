from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import data_required

class DataForm(FlaskForm):
    text = StringField('Text:', validators=[data_required()])
    submit = SubmitField('Submit')