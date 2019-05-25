'''Routes for main BP'''

from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_required
from app import DB as db
from app.main.forms import EditProfileForm
from app.models import User
from app.main import BP as bp

@bp.before_request
def before_request():
    '''Routines to store user activity'''
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@bp.route('/')
@bp.route('/index')
def index():
    '''Site index'''
    return render_template('index.html')


@bp.route('/secure')
@login_required
def secure():
    '''secure page'''
    return render_template('index.html')


@bp.route('/user/<username>')
@login_required
def user(username):
    '''User profile screen'''
    _user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=_user)



@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    '''Editr profile screen'''
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.full_name = form.full_name.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.full_name.data = current_user.full_name
    return render_template('edit_profile.html', title='Edit Profile', form=form)
