'''Main app forms'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField,PasswordField
#from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
#from wtforms.validators import EqualTo