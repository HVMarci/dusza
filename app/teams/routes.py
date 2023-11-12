from flask import render_template, flash, redirect, url_for, abort
from pymysql import IntegrityError

from app.models.team import Team
from app.models.user import User
from app.security import has_role, is_fully_authenticated
from app.teams import bp
from app.teams.forms import TeamForm


@bp.route('/')
@is_fully_authenticated
def list_teams():
    teams = Team.find_all()

    return render_template('teams/list.html', teams=teams)


@bp.route('/create', methods=('get', 'post'))
@has_role('ADMIN')
def create_team():
    return abort(503)
    ''''
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
    '''

@bp.route('/edit/<team_id>', methods=('get', 'post'))
@has_role('ADMIN')
def edit_team(team_id):
    team = Team.find_by_id(team_id) or abort(404)
    form = TeamForm(
        team_name=team.team_name,
        description=team.description,
        evfolyam=team.evfolyam,
        osztaly=team.osztaly,
        user_ids=tuple([user.user_id for user in User.find_by_team(team.id)])
    )

    if form.validate_on_submit():
        try:
            team.team_name = form.team_name
            team.description = form.description
            team.evfolyam = form.evfolyam
            team.osztaly = form.osztaly
            team.user_ids = form.user_ids

            Team.save(team)
            for user_id in team.user_ids:
                user = User.find_by_id(user_id)
                user.team_id = team.id
                User.save(user)

            flash('Csapat elmentve.')

            return redirect(url_for('teams.edit_team', team_id=team_id))
        except IntegrityError as e:
            form.errors.append(str(e))

    return render_template('teams/edit.html', form=form, find_by_evfolyam=User.find_by_evfolyam)


@bp.route('/delete/<team_id>', methods=('post',))
@has_role('ADMIN')
def delete_team(team_id):
    team = Team.find_by_id(team_id) or abort(404)

    try:
        Team.delete(team.id)
        flash('Csapat törölve.')
    except IntegrityError as e:
        flash(str(e))

    return redirect(url_for('teams.list_teams'))

