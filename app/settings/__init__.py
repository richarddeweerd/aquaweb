'''BP init for Settings module'''
from flask import Blueprint


BP = Blueprint('Settings', __name__)
#pylint: disable=wrong-import-position
from app.settings import routes
#pylint: enable=wrong-import-position
