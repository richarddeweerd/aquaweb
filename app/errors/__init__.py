'''BP init for error module'''

from flask import Blueprint
from app.errors import handlers
BP = Blueprint('errors', __name__)
