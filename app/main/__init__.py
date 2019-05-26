'''BP init for Main module'''
from flask import Blueprint

BP = Blueprint('main', __name__)

#pylint: disable=wrong-import-position
from app.main import routes
#pylint: enable=wrong-import-position
