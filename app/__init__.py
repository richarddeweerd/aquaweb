'''Init for Main app'''

import os
import logging
from logging.handlers import RotatingFileHandler, SMTPHandler

from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from app.config import Config


DB = SQLAlchemy()
MIGRATE = Migrate()
LOGIN = LoginManager()
LOGIN.login_view = 'login'
MAIL = Mail()
BOOTSTRAP = Bootstrap()


def create_app(config_class=Config):
    '''Init app'''
    app = Flask(__name__)
    app.config.from_object(config_class)

    DB.init_app(app)
    MIGRATE.init_app(app, DB)
    LOGIN.init_app(app)
    MAIL.init_app(app)
    BOOTSTRAP.init_app(app)

    from app.admin import BP as admin_bp
    app.register_blueprint(admin_bp)

    from app.auth import BP as auth_bp
    app.register_blueprint(auth_bp)

    from app.errors import BP as errors_bp
    app.register_blueprint(errors_bp)

    from app.main import BP as main_bp
    app.register_blueprint(main_bp)


    if not app.debug:

        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/aquaweb.log', maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('AquaWeb startup')

        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'][1], subject='AquaWeb Failure',
                credentials=auth, secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)
    return app

#pylint: disable=wrong-import-position
from app import models
#pylint: enable=wrong-import-position
