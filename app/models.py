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


class TempHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    t0 = db.Column(db.Float)
    t1 = db.Column(db.Float)
    t2 = db.Column(db.Float)
    t3 = db.Column(db.Float)
    t4 = db.Column(db.Float)
    time = db.Column(db.DateTime, default=datetime.utcnow)


class ReefConfig(db.Model):
    '''Configuration class definition'''
    id = db.Column(db.Integer, primary_key=True)
    t0 = db.Column(db.String(20))
    t1 = db.Column(db.String(20))
    t2 = db.Column(db.String(20))
    t3 = db.Column(db.String(20))
    t4 = db.Column(db.String(20))
    t1_name = db.Column(db.String(32))
    t2_name = db.Column(db.String(32))
    t3_name = db.Column(db.String(32))
    t4_name = db.Column(db.String(32))
    o1_name = db.Column(db.String(32))
    o2_name = db.Column(db.String(32))
    o3_name = db.Column(db.String(32))
    o4_name = db.Column(db.String(32))
    o5_name = db.Column(db.String(32))
    o6_name = db.Column(db.String(32))
    o7_name = db.Column(db.String(32))
    o8_name = db.Column(db.String(32))
    o9_name = db.Column(db.String(32))
    o10_name = db.Column(db.String(32))
    o11_name = db.Column(db.String(32))
    o12_name = db.Column(db.String(32))
    o13_name = db.Column(db.String(32))
    o14_name = db.Column(db.String(32))
    o15_name = db.Column(db.String(32))
    o16_name = db.Column(db.String(32))
    o17_name = db.Column(db.String(32))
    o18_name = db.Column(db.String(32))
    o19_name = db.Column(db.String(32))
    o20_name = db.Column(db.String(32))
    o21_name = db.Column(db.String(32))
    o22_name = db.Column(db.String(32))
    o23_name = db.Column(db.String(32))
    o24_name = db.Column(db.String(32))
    o25_name = db.Column(db.String(32))
    o26_name = db.Column(db.String(32))
    o27_name = db.Column(db.String(32))
    o28_name = db.Column(db.String(32))
    o29_name = db.Column(db.String(32))
    o30_name = db.Column(db.String(32))
    o31_name = db.Column(db.String(32))
    o32_name = db.Column(db.String(32))
    
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)


class UserLevel(db.Model):
    '''User level class definition'''
    id = db.Column(db.Integer, primary_key=True)
    levelname = db.Column(db.String(64), index=True, unique=True)
    users = db.relationship('User', backref='level', lazy='dynamic')

    def __repr__(self):
        return '<Level {}>'.format(self.levelname)


class User(UserMixin, db.Model):
    '''User class definition'''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    full_name = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    level_id = db.Column(db.Integer, db.ForeignKey('user_level.id'))

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
