from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from app import db
from app.admin import bp
from app.models import User

@bp.route('/admin/accounts')
def accounts():

    # User is the name of table that has a column name
    accounts = User.query.all()

    return render_template('admin/accounts.html', accounts=accounts)
    

@bp.route('/admin/measure')
def measure():
    return render_template('admin/measure.html')