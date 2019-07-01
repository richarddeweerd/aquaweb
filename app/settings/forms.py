'''Main app forms'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,PasswordField
#from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
#from wtforms.validators import EqualTo

class TemperatureForm(FlaskForm):
    '''Form to edit the Temperature sensors'''
    t0 = SelectField('t0', coerce=str)
    t1 = SelectField('t1', coerce=str)
    t2 = SelectField('t2', coerce=str)
    t3 = SelectField('t3', coerce=str)
    t4 = SelectField('t4', coerce=str)
    submit = SubmitField('Submit')
