'''Routes for main BP'''

import json

from datetime import datetime
from flask import render_template, jsonify
from flask_login import current_user, login_required
from app import DB as db
#from flask import render_template, flash, redirect, url_for, request
from app.functions import file_to_dict

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


@bp.route('/data/current')
#@login_required
def current_data():
    '''json data page'''
    data = {}
    data["analog"] = file_to_dict("/var/aquarium/analog")
    #data["status"] = file_to_dict("/var/aquarium/status")
    data["moon"] = file_to_dict("/var/aquarium/moon")
    data["baro"] = file_to_dict("/var/aquarium/baro")
    data["config"] = file_to_dict("/var/aquarium/config")
    data["temperature"] = file_to_dict("/var/aquarium/temperature")
    return jsonify(data)

@bp.route('/data/rawtemp')
#@login_required
def data_rawtemp():
    '''json data page'''
    data = file_to_dict("/var/aquarium/rawtemp")
    return jsonify(data)
