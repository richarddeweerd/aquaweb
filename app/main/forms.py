'''Main app forms'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
#from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
#from wtforms.validators import DataRequired, Email, EqualTo, Length

class EditProfileForm(FlaskForm):
    '''Form to edit the user profile '''
    username = StringField('Username', validators=[DataRequired()])
    full_name = StringField('Full name', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')
