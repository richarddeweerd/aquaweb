'''Models definitions'''
from datetime import datetime
from time import time
from hashlib import md5

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import jwt

from flask import current_app

from app import DB as db
from app import LOGIN as login

class User(UserMixin, db.Model):
    '''User class definition'''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    full_name = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    level = db.Column(db.Integer)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        '''Set user password'''
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        '''Check user password'''
        return check_password_hash(self.password_hash, password)

    def get_reset_password_token(self, expires_in=600):
        '''Generate JWT token'''
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            current_app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_reset_password_token(token):
        '''Verify JWT token'''
        try:
            jwtresult = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
        except jwt.DecodeError:
            return
        return User.query.get(jwtresult)

    def avatar(self, size):
        '''Generate Gravatar link'''
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)


@login.user_loader
def load_user(uid):
    '''Flask-Login user loader function'''
    return User.query.get(int(uid))
