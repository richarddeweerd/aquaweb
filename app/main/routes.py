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
    data = {}

    try:
        with open(fname) as json_file:  
            data = json.load(json_file)
    except:
        pass
    return data

@bp.route('/data/current')
#@login_required
def current_data():
    '''json data page'''
    data = {}
    data["moon"] = file_to_dict("/var/aquarium/temperature")
    data["raw"] = {"temperature" : file_to_dict("/var/aquarium/temperature")}

    return jsonify(data)



