'''Admin module routes'''
from flask import render_template
from flask_login import login_required
from app.settings import BP as bp

#from flask import render_template, redirect, flash, request, url_for
#from werkzeug.urls import url_parse
#from flask_login import login_user, logout_user, current_user
#from app import DB as db

#from app.models import User, UserLevel



@bp.route('/settings/parameters')
@login_required
def measure():
    '''Screen with measurment types list'''
    return render_template('admin/parameters.html')

@bp.route('/settings/outputs')
@login_required
def measure():
    '''Screen with measurment types list'''
    return render_template('admin/outputs.html')

@bp.route('/settings/temperature')
@login_required
def measure():
    '''Screen with measurment types list'''
    return render_template('admin/temperature.html')
