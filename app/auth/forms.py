'''Auth module forms'''
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length
#from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
#from app.models import User

class EditProfileForm(FlaskForm):
    '''Form to edit the user profile '''
    username = StringField('Username', validators=[DataRequired()])
    full_name = StringField('Full name', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    '''Form for logging in'''
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ResetPasswordRequestForm(FlaskForm):
    '''Form to request PWD change'''
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    '''PWD change form'''
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')

class ChangePasswordForm(FlaskForm):
    '''PWD change form'''
    password = PasswordField('Current password', validators=[DataRequired()])
    newpwd = PasswordField('New Password', validators=[DataRequired()])
    newpwd2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('newpwd')])
    submit = SubmitField('Request Password Reset')

class EditAccountForm(FlaskForm):
    '''Form to edit the user profile '''
    username = StringField('Username', validators=[DataRequired()])
    full_name = StringField('Full name', validators=[Length(min=0, max=140)])
    email = StringField('Email', validators=[Email(), DataRequired()])
    level = SelectField('Level', coerce=int)
    submit = SubmitField('Submit')

class SetAccountPasswordForm(FlaskForm):
    '''PWD set form'''
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')
