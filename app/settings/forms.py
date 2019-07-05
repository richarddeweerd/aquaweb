'''Main app forms'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,PasswordField
#from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
#from wtforms.validators import EqualTo

class TemperatureForm(FlaskForm):
    '''Form to edit the Temperature sensors'''
    t0 = SelectField('Temp0', coerce=str, validators=[Length(min=0, max=32)])
    t1 = SelectField('t1', coerce=str, validators=[Length(min=0, max=32)])
    t2 = SelectField('t2', coerce=str, validators=[Length(min=0, max=32)])
    t3 = SelectField('t3', coerce=str, validators=[Length(min=0, max=32)])
    t4 = SelectField('t4', coerce=str, validators=[Length(min=0, max=32)])
    t1_name = StringField('Sensor_1_name', validators=[Length(min=0, max=32)])
    t2_name = StringField('Sensor_2_name', validators=[Length(min=0, max=32)])
    t3_name = StringField('Sensor_3_name', validators=[Length(min=0, max=32)])
    t4_name = StringField('Sensor_4_name', validators=[Length(min=0, max=32)])
    submit = SubmitField('Submit')
