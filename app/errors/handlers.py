'''Handlers for errors'''
from flask import render_template
from app import DB as db
from app.errors import BP as bp

@bp.app_errorhandler(404)
def not_found_error(error):
    '''404 Error'''
    return render_template('errors/404.html', err=error), 404


@bp.app_errorhandler(500)
def internal_error(error):
    '''500 Error'''
    db.session.rollback()
    return render_template('errors/500.html', err=error), 500
