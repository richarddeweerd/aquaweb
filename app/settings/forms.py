'''Main app forms'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,PasswordField
#from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
#from wtforms.validators import EqualTo

class OutputsForm(FlaskForm):
    '''Form to edit the Output names'''
    o1_name = StringField('Output 1', validators=[Length(min=0, max=32)])
    o2_name = StringField('Output 2', validators=[Length(min=0, max=32)])
    o3_name = StringField('Output 3', validators=[Length(min=0, max=32)])
    o4_name = StringField('Output 4', validators=[Length(min=0, max=32)])
    o5_name = StringField('Output 5', validators=[Length(min=0, max=32)])
    o6_name = StringField('Output 6', validators=[Length(min=0, max=32)])
    o7_name = StringField('Output 7', validators=[Length(min=0, max=32)])
    o8_name = StringField('Output 8', validators=[Length(min=0, max=32)])
    o9_name = StringField('Output 9', validators=[Length(min=0, max=32)])
    o10_name = StringField('Output 10', validators=[Length(min=0, max=32)])
    o11_name = StringField('Output 11', validators=[Length(min=0, max=32)])
    o12_name = StringField('Output 12', validators=[Length(min=0, max=32)])
    o13_name = StringField('Output 13', validators=[Length(min=0, max=32)])
    o14_name = StringField('Output 14', validators=[Length(min=0, max=32)])
    o15_name = StringField('Output 15', validators=[Length(min=0, max=32)])
    o16_name = StringField('Output 16', validators=[Length(min=0, max=32)])
    o17_name = StringField('Output 17', validators=[Length(min=0, max=32)])
    o18_name = StringField('Output 18', validators=[Length(min=0, max=32)])
    o19_name = StringField('Output 19', validators=[Length(min=0, max=32)])
    o20_name = StringField('Output 20', validators=[Length(min=0, max=32)])
    o21_name = StringField('Output 21', validators=[Length(min=0, max=32)])
    o22_name = StringField('Output 22', validators=[Length(min=0, max=32)])
    o23_name = StringField('Output 23', validators=[Length(min=0, max=32)])
    o24_name = StringField('Output 24', validators=[Length(min=0, max=32)])
    o25_name = StringField('Output 25', validators=[Length(min=0, max=32)])
    o26_name = StringField('Output 26', validators=[Length(min=0, max=32)])
    o27_name = StringField('Output 27', validators=[Length(min=0, max=32)])
    o28_name = StringField('Output 28', validators=[Length(min=0, max=32)])
    o29_name = StringField('Output 29', validators=[Length(min=0, max=32)])
    o30_name = StringField('Output 30', validators=[Length(min=0, max=32)])
    o31_name = StringField('Output 31', validators=[Length(min=0, max=32)])
    o32_name = StringField('Output 32', validators=[Length(min=0, max=32)])
    submit = SubmitField('Submit')


class TemperatureForm(FlaskForm):
    '''Form to edit the Temperature sensors'''
    t0 = SelectField('Temp0', validators=[Length(min=0, max=32)])
    t1 = SelectField('t1', validators=[Length(min=0, max=32)])
    t2 = SelectField('t2', validators=[Length(min=0, max=32)])
    t3 = SelectField('t3', validators=[Length(min=0, max=32)])
    t4 = SelectField('t4', validators=[Length(min=0, max=32)])
    t1_name = StringField('Sensor_1_name', validators=[Length(min=0, max=32)])
    t2_name = StringField('Sensor_2_name', validators=[Length(min=0, max=32)])
    t3_name = StringField('Sensor_3_name', validators=[Length(min=0, max=32)])
    t4_name = StringField('Sensor_4_name', validators=[Length(min=0, max=32)])

    submit = SubmitField('Submit')
