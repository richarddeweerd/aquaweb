'''Routes for main BP'''

import json

from datetime import datetime
from flask import render_template, jsonify
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

def file_to_dict(fname):
    '''Read json file and return dictionary'''
    data = {}

    try:
        with open(fname) as json_file:
            data = json.load(json_file)
    except IOError:
        data["error"] = "No data file"

    return data

@bp.route('/data/current')
#@login_required
def current_data():
    '''json data page'''
    data = {}
    data["status"] = file_to_dict("/var/aquarium/status")
    data["moon"] = file_to_dict("/var/aquarium/moon")
    data["baro"] = file_to_dict("/var/aquarium/baro")
    data["config"] = {"devices" : file_to_dict("/var/aquarium/config/devices")}
    rawdat = {}
    rawdat["temperature"] = file_to_dict("/var/aquarium/rawdata/temperature")
    rawdat["analog"] = file_to_dict("/var/aquarium/rawdata/analog")
    data["raw"] = rawdat
    return jsonify(data)
