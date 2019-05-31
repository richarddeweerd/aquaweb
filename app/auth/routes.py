'''Auth module routes'''

from flask import render_template, redirect, url_for, flash, request
#from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user, login_required
from app import DB as db
from app.auth import BP as bp
from app.auth.forms import LoginForm, ResetPasswordRequestForm, ResetPasswordForm, EditAccountForm, EditProfileForm, SetAccountPasswordForm, ChangePasswordForm
from app.models import User, UserLevel
from app.auth.email import send_password_reset_email

@bp.route('/login', methods=['GET', 'POST'])
def login():
    '''Route to login'''
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('main.index'))
    return render_template('auth/login.html', title='Sign In', form=form)

@bp.route('/logout')
def logout():
    '''rout to logout'''
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    '''Route for pwd reset request'''
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password_request.html',
                           title='Reset Password', form=form)

@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    '''Route for pwd reset'''
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('main.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)

@bp.route('/view_profile')
@login_required
def view_profile():
    '''View profile screen'''
    return render_template('auth/view_profile.html', user=current_user)


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    '''Edit profile screen'''
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
    return render_template('auth/edit_profile.html', title='Edit Profile', form=form)

@bp.route('/change_pwd', methods=['GET', 'POST'])
@login_required
def change_pwd():
    '''Set profile pwd'''
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.check_password(form.password.data):
            current_user.set_password(form.newpwd.data)
            db.session.commit()
            flash('Your changes have been saved.')
        else:
            flash('Wrong password.')
            return redirect(url_for('auth.change_pwd'))
        return redirect(url_for('main.index'))

    return render_template('auth/change_password.html', title='Edit Profile', form=form)


@bp.route('/admin/accounts')
@login_required
def accounts():
    '''Screen with account list'''
    # User is the name of table that has a column name
    _accounts = User.query.all()

    return render_template('auth/admin/accounts.html', title="Accounts", accounts=_accounts)


@bp.route('/admin/edit_account/<uid>', methods=['GET', 'POST'])
@login_required
def edit_account(uid):
    '''User account edit screen'''
    _account = User.query.filter_by(id=uid).first_or_404()

    form = EditAccountForm()
    form.level.choices = [(l.id, l.levelname) for l in UserLevel.query.order_by('id')]

    if form.validate_on_submit():
        _account.username = form.username.data
        _account.full_name = form.full_name.data
        _account.email = form.email.data
        if _account.id != current_user.id:
            _account.level_id = form.level.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('admin.accounts'))
    elif request.method == 'GET':
        form.username.data = _account.username
        form.full_name.data = _account.full_name
        form.email.data = _account.email
        form.level.data = _account.level_id

    return render_template('auth/admin/edit_account.html', uid=uid, title='Edit Account', form=form)


@bp.route('/admin/set_pwd/<uid>', methods=['GET', 'POST'])
@login_required
def set_account_password(uid):
    '''User account edit screen'''
    _account = User.query.filter_by(id=uid).first_or_404()

    form = SetAccountPasswordForm()

    if form.validate_on_submit():
        _account.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('auth.accounts'))


    return render_template('auth/admin/set_password.html', uid=uid, title='Set Password', form=form, account=_account)
