'''Admin module routes'''
from flask import render_template
from flask_login import login_required
from app.admin import BP as bp

#from flask import render_template, redirect, flash, request, url_for
#from werkzeug.urls import url_parse
#from flask_login import login_user, logout_user, current_user
#from app import DB as db

#from app.models import User, UserLevel



@bp.route('/admin/measure')
@login_required
def measure():
    '''Screen with measurment types list'''
    return render_template('admin/measure.html')
