'''Routes for main BP'''

from datetime import datetime
from flask import render_template
from flask_login import current_user, login_required
from app import DB as db
#from flask import render_template, flash, redirect, url_for, request

#from app.models import User
from app.main import BP as bp

@bp.before_request
def before_request():
    '''Routines to store user activity'''
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@bp.route('/')
@bp.route('/index')
def index():
    '''Site index'''
    return render_template('index.html')


@bp.route('/secure')
@login_required
def secure():
    '''secure page'''
    return render_template('index.html')
