'''Admin module routes'''
from flask import render_template
#from flask import render_template, redirect, url_for, flash, request
#from werkzeug.urls import url_parse
#from flask_login import login_user, logout_user, current_user
#from app import DB as db
from app.admin import BP as bp
from app.models import User

@bp.route('/admin/accounts')
def accounts():
    '''Screen with account list'''
    # User is the name of table that has a column name
    _accounts = User.query.all()

    return render_template('admin/accounts.html', accounts=_accounts)


@bp.route('/admin/measure')
def measure():
    '''Screen with measurment types list'''
    return render_template('admin/measure.html')
