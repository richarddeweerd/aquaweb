'''Settings module routes'''
from flask import render_template, redirect, url_for, flash, request

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

@bp.route('/settings/temperature', methods=['GET', 'POST'])
@login_required
def temperature():
    '''Screen to link temperature sensors'''
    cfgdata = ReefConfig.query.filter_by(id=1).first_or_404()
    rawdata = file_to_dict("/var/aquarium/rawtemp")
    form = TemperatureForm()

    senlist = []
    sensoritem = ("none", "None")
    senlist.append(sensoritem)
    for sens in rawdata:
        sensoritem = (sens["id"], sens["id"])
        senlist.append(sensoritem)


    if form.validate_on_submit():
        #_account.username = form.username.data
        #_account.full_name = form.full_name.data
        #_account.email = form.email.data
        #if _account.id != current_user.id:
        #    _account.level_id = form.level.data
        #db.session.commit()
        flash('Your changes have been saved.')
        #return render_template('settings/temperature.html', title='Temperature sensor setup', form=form, sensors=rawdata)

    elif request.method == 'GET':
        form.t0.choices = senlist
        form.t1.choices = senlist
        form.t2.choices = senlist
        form.t3.choices = senlist
        form.t4.choices = senlist
        form.t1_name.data = cfgdata.t1_name
        form.t2_name.data = cfgdata.t2_name
        form.t3_name.data = cfgdata.t3_name
        form.t4_name.data = cfgdata.t4_name
    return render_template('settings/temperature.html', title='Temperature sensor setup', form=form, sensors=rawdata)
