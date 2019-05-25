'''BP init for error module'''

from flask import Blueprint

BP = Blueprint('errors', __name__)

#pylint: disable=wrong-import-position
from app.errors import handlers
#pylint: enable=wrong-import-position
