'''BP init for Admin module'''
from flask import Blueprint


BP = Blueprint('admin', __name__)
#pylint: disable=wrong-import-position
from app.admin import routes
#pylint: enable=wrong-import-position
