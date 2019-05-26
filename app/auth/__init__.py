'''BP init for authentication module'''
from flask import Blueprint

BP = Blueprint('auth', __name__)

#pylint: disable=wrong-import-position
from app.auth import routes
#pylint: enable=wrong-import-position
