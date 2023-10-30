from flask import render_template, flash, redirect, url_for, abort
from pymysql import IntegrityError

from app.models.role import Role
from app.models.user import User
from app.roles import bp
from app.roles.forms import RoleForm, RoleUserForm
from app.security import has_role


@bp.route('/')
@has_role('ADMIN')
def list_roles():
    roles = Role.find_all()

    return render_template('roles/list.html', roles=roles)


@bp.route('/create', methods=('get', 'post'))
@has_role('ADMIN')
def create_role():
    form = RoleForm(
        create=True
    )

    if form.validate_on_submit():
        try:
            role = Role(
                name=form.name
            )

            Role.save(role)
            flash('Role created.')

            return redirect(url_for('roles.list_roles'))
        except IntegrityError as e:
            form.errors.append(str(e))

    return render_template('roles/edit.html', form=form)


@bp.route('/edit/<name>', methods=('get', 'post'))
@has_role('ADMIN')
def edit_role(name):
    role = Role.find_by_name(name) or abort(404)
    form = RoleForm(
        name=role.name
    )

    if form.validate_on_submit():
        try:
            role.name = form.name

            Role.save(role)
            flash('Role saved.')

            return redirect(url_for('roles.edit_role', name=role.name))
        except IntegrityError as e:
            form.errors.append(str(e))

    return render_template('roles/edit.html', form=form, role=role)


@bp.route('/delete/<name>', methods=('post',))
@has_role('ADMIN')
def delete_role(name):
    role = Role.find_by_name(name) or abort(404)

    try:
        Role.delete(role.role_id)
        flash('Role deleted.')
    except IntegrityError as e:
        flash(str(e))

    return redirect(url_for('roles.list_roles'))


@bp.route('/create-user/<name>', methods=('get', 'post'))
@has_role('ADMIN')
def create_role_user(name):
    role = Role.find_by_name(name) or abort(404)
    form = RoleUserForm(
        create=True
    )

    if form.validate_on_submit():
        try:
            user = User(
                username=form.username,
                password=form.password,
                role_id=role.role_id
            )

            User.save(user)
            flash('User created.')

            return redirect(url_for('roles.edit_role', name=role.name))
        except IntegrityError as e:
            form.errors.append(str(e))

    return render_template('roles/edit_user.html', form=form, role=role)


@bp.route('/edit-user/<name>/<username>', methods=('get', 'post'))
@has_role('ADMIN')
def edit_role_user(name, username):
    role = Role.find_by_name(name) or abort(404)
    user = User.find_by_username_and_role_id(username, role.role_id) or abort(404)

    form = RoleUserForm(
        username=user.username
    )

    if form.validate_on_submit():
        try:
            user.username = form.username
            user.password = form.password

            User.save(user)
            flash('User saved.')

            return redirect(url_for('roles.edit_role_user', name=role.name, username=user.username))
        except IntegrityError as e:
            form.errors.append(str(e))

    return render_template('roles/edit_user.html', form=form, role=role)


@bp.route('/delete-user/<name>/<username>', methods=('post',))
@has_role('ADMIN')
def delete_role_user(name, username):
    role = Role.find_by_name(name) or abort(404)
    user = User.find_by_username_and_role_id(username, role.role_id) or abort(404)

    try:
        User.delete(user.user_id)
        flash('User deleted.')
    except IntegrityError as e:
        flash(str(e))

    return redirect(url_for('roles.edit_role', name=role.name))
