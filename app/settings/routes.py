'''Settings module routes'''
from flask import render_template
from flask_login import login_required
from app.settings import BP as bp
from app.settings.forms import TemperatureForm
#from flask import render_template, redirect, flash, request, url_for
#from werkzeug.urls import url_parse
#from flask_login import login_user, logout_user, current_user
#from app import DB as db

from app.functions import file_to_dict

from app.models import ReefConfig



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
    cfgdata = ReefConfig.query.filter_by(id=1).first_or_404()

    rawdata = file_to_dict("/var/aquarium/rawtemp")

    form = TemperatureForm()
    #form.level.choices = [(l.id, l.levelname) for l in UserLevel.query.order_by('id')]
    senlist = []
    sensoritem = ("none", "None")
    senlist.append(sensoritem)
    for sens in rawdata:
        sensoritem = (sens["id"], sens["id"])
        senlist.append(sensoritem)

    form.t0.choices = senlist
    form.t1.choices = senlist
    form.t2.choices = senlist
    form.t3.choices = senlist
    form.t4.choices = senlist
    form.t1_name.data = cfgdata.t1_name
    return render_template('settings/temperature.html', title='Temperature sensor setup', form=form)
