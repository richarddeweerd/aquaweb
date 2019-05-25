'''BP init for authentication module'''
from flask import Blueprint
from app.auth import routes

BP = Blueprint('auth', __name__)
