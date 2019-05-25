'''BP init for Admin module'''
from flask import Blueprint
from app.admin import routes

BP = Blueprint('admin', __name__)
