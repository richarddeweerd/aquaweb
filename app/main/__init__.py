'''BP init for Main module'''
from flask import Blueprint
from app.main import routes

BP = Blueprint('main', __name__)
