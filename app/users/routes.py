from flask import render_template, flash, redirect, url_for, abort
from pymysql import IntegrityError

from app.models.role import Role
from app.models.user import User
from app.security import is_fully_authenticated, has_role
from app.users import bp
from app.users.forms import UserForm


@bp.route('/')
@is_fully_authenticated
def list_users():
    users = User.find_all()

    return render_template('users/list.html', users=users)


@bp.route('/create', methods=('get', 'post'))
@has_role('ADMIN')
def create_user():
    form = UserForm(
        create=True
    )

    if form.validate_on_submit():
        try:
            user = User(
                username=form.username,
                password=form.password,
                role_id=form.role_id,
                evfolyam=form.evfolyam,
                osztaly=form.osztaly
            )

            User.save(user)
            flash('User created.')

            return redirect(url_for('users.list_users'))
        except IntegrityError as e:
            form.errors.append(str(e))

    roles = Role.find_all()

    print(form.evfolyam, form.osztaly)
    return render_template('users/edit.html', form=form, roles=roles)


@bp.route('/edit/<username>', methods=('get', 'post'))
@has_role('ADMIN')
def edit_user(username):
    user = User.find_by_username(username) or abort(404)
    form = UserForm(
        username=user.username,
        role_id=user.role_id,
        evfolyam=user.evfolyam,
        osztaly=user.osztaly
    )

    if form.validate_on_submit():
        try:
            user.username = form.username
            user.password = form.password
            user.role_id = form.role_id
            user.evfolyam = form.evfolyam
            user.osztaly = form.osztaly

            User.save(user)
            flash('User saved.')

            return redirect(url_for('users.edit_user', username=username))
        except IntegrityError as e:
            form.errors.append(str(e))

    roles = Role.find_all()

    return render_template('users/edit.html', form=form, roles=roles)


@bp.route('/delete/<username>', methods=('post',))
@has_role('ADMIN')
def delete_user(username):
    user = User.find_by_username(username) or abort(404)

    try:
        User.delete(user.user_id)
        flash('User deleted.')
    except IntegrityError as e:
        flash(str(e))

    return redirect(url_for('users.list_users'))
