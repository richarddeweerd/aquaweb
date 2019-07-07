'''Settings module routes'''

from datetime import datetime

from flask import render_template, redirect, url_for, flash, request

from flask_login import login_required
from app.settings import BP as bp
from app import DB as db

from app.settings.forms import TemperatureForm, OutputsForm
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

@bp.route('/settings/outputs', methods=['GET', 'POST'])
@login_required
def outputs():
    '''Screen to set ouput names'''
    cfgdata = ReefConfig.query.filter_by(id=1).first_or_404()

    form = OutputsForm()

    if form.validate_on_submit():
        flash('Your changes have been saved.')

    elif request.method == 'GET':

        form.o1_name.data = cfgdata.o1_name
        form.o2_name.data = cfgdata.o2_name
        form.o3_name.data = cfgdata.o3_name
        form.o4_name.data = cfgdata.o4_name
        form.o5_name.data = cfgdata.o5_name
        form.o6_name.data = cfgdata.o6_name
        form.o7_name.data = cfgdata.o7_name
        form.o8_name.data = cfgdata.o8_name
        form.o9_name.data = cfgdata.o9_name
        form.o10_name.data = cfgdata.o10_name
        form.o11_name.data = cfgdata.o11_name
        form.o12_name.data = cfgdata.o12_name
        form.o13_name.data = cfgdata.o13_name
        form.o14_name.data = cfgdata.o14_name
        form.o15_name.data = cfgdata.o15_name
        form.o16_name.data = cfgdata.o16_name
        form.o17_name.data = cfgdata.o17_name
        form.o18_name.data = cfgdata.o18_name
        form.o19_name.data = cfgdata.o19_name
        form.o20_name.data = cfgdata.o20_name
        form.o21_name.data = cfgdata.o21_name
        form.o22_name.data = cfgdata.o22_name
        form.o23_name.data = cfgdata.o23_name
        form.o24_name.data = cfgdata.o24_name
        form.o25_name.data = cfgdata.o25_name
        form.o26_name.data = cfgdata.o26_name
        form.o27_name.data = cfgdata.o27_name
        form.o28_name.data = cfgdata.o28_name
        form.o29_name.data = cfgdata.o29_name
        form.o30_name.data = cfgdata.o30_name
        form.o31_name.data = cfgdata.o31_name
        form.o32_name.data = cfgdata.o32_name

    return render_template('settings/outputs.html', title='Output setup', form=form)

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

    form.t0.choices = senlist
    form.t1.choices = senlist
    form.t2.choices = senlist
    form.t3.choices = senlist
    form.t4.choices = senlist

    if form.validate_on_submit():

        if form.t0.data == "none":
            cfgdata.t0 = ""
        else:
            cfgdata.t0 = form.t0.data

        if form.t1.data == "none":
            cfgdata.t1 = ""
        else:
            cfgdata.t1 = form.t1.data

        if form.t2.data == "none":
            cfgdata.t2 = ""
        else:
            cfgdata.t2 = form.t2.data

        if form.t3.data == "none":
            cfgdata.t3 = ""
        else:
            cfgdata.t3 = form.t3.data

        if form.t4.data == "none":
            cfgdata.t4 = ""
        else:
            cfgdata.t4 = form.t4.data


        cfgdata.t1_name = form.t1_name.data
        cfgdata.t2_name = form.t2_name.data
        cfgdata.t3_name = form.t3_name.data
        cfgdata.t4_name = form.t4_name.data
        cfgdata.last_updated = datetime.utcnow()
        db.session.commit()
        flash('Your changes have been saved.')

    elif request.method == 'GET':
        form.t0.data = cfgdata.t0
        form.t1.data = cfgdata.t1
        form.t2.data = cfgdata.t2
        form.t3.data = cfgdata.t3
        form.t4.data = cfgdata.t4

        form.t1_name.data = cfgdata.t1_name
        form.t2_name.data = cfgdata.t2_name
        form.t3_name.data = cfgdata.t3_name
        form.t4_name.data = cfgdata.t4_name
    return render_template('settings/temperature.html', title='Temperature sensor setup', form=form, sensors=rawdata)
