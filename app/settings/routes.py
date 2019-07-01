'''Settings module routes'''
from flask import render_template
from flask_login import login_required
from app.settings import BP as bp
from app.settings.forms import TemperatureForm
#from flask import render_template, redirect, flash, request, url_for
#from werkzeug.urls import url_parse
#from flask_login import login_user, logout_user, current_user
#from app import DB as db

#from app.models import User, UserLevel



@bp.route('/settings/parameters')
@login_required
def parameters():
    '''Screen with measurment types list'''
    return render_template('settings/parameters.html')

@bp.route('/settings/outputs')
@login_required
def outputs():
    '''Screen with measurment types list'''
    return render_template('settings/outputs.html')

@bp.route('/settings/temperature')
@login_required
def temperature():
    '''Screen to link temperature sensors'''
    form = TemperatureForm()
    #form.level.choices = [(l.id, l.levelname) for l in UserLevel.query.order_by('id')]

    senlist = [('Sensor 1', 'Sensor 1'), ('Sensor 2', 'Sensor 2'), ('Sensor 3', 'Sensor 3')]
    form.t0.choices = senlist
    form.t1.choices = senlist
    form.t2.choices = senlist
    form.t3.choices = senlist
    form.t4.choices = senlist

    return render_template('settings/temperature.html', title='Temperature sensor setup', form=form)
