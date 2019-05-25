'''File to launch the app'''
from app import create_app

APP = create_app()

APP.run(host='0.0.0.0')
