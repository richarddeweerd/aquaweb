from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from app import db
from app.admin import bp


@bp.route('/admin/accounts')
def accounts():
    #return render_template('index.html')
    return "admin page"