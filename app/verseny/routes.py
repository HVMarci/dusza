from random import random, randint

from app.models.feladat import Feladat
from app.models.verseny import Verseny
from app.verseny import bp

from flask import render_template, flash, redirect, url_for, abort, g, request
from pymysql import IntegrityError

from app.models.role import Role
from app.models.user import User
from app.models.team import Team
from app.roles.forms import RoleForm, RoleUserForm
from app.security import has_role, is_fully_authenticated
from time import time
from datetime import datetime

from app.verseny.forms import VersenyForm


def format_epoch(epoch_time):
    return datetime.fromtimestamp(epoch_time).strftime("%Y-%m-%d %H:%M:%S")


@bp.route('/')
@is_fully_authenticated
def verseny_list():
    versenyek = []
    if g.user.role.name == 'ZSURI' or g.user.role.name == 'ADMIN':
        versenyek += Verseny.find_all()
    elif g.user.team_id and g.user.team.verseny_id:
        versenyek.append(Verseny.find_by_id(g.user.team.verseny_id))

    return render_template('verseny/list.html', versenyek=versenyek, time=time, format_epoch=format_epoch)

@bp.route('/play/<id>', methods=('get', 'post'))
@has_role('DIAK')
def verseny_play(id):
    feladat, hossz = Feladat.find_by_progress(g.user.progress, g.user.team.verseny_id)

    if g.user.progress >= hossz:
        flash('Vége a versenynek!')
        return redirect(url_for('verseny.verseny_list'))

    if request.method == 'POST':
        if request.form.get('megoldas') == feladat.strings[3]:
            g.user.helyes += 1
        g.user.progress += 3
        User.save(g.user)

        return redirect(url_for('verseny.verseny_play', id=g.user.team.verseny_id))

    return render_template('verseny/play.html', feladat=feladat)


@bp.route('/create', methods=('get', 'post'))
@has_role('ZSURI')
def create_verseny():
    form = VersenyForm(
        create=True
    )
    feladatok = Feladat.find_all()

    if form.validate_on_submit():
        try:
            verseny = Verseny(
                name=form.name,
                description=form.description,
                kezdet=form.kezdet,
                veg=form.veg,
                evfolyam=form.evfolyam
            )

            Verseny.save(verseny)

            flash('Verseny létrehozva.')

            return redirect(url_for('verseny.verseny_list'))
        except IntegrityError as e:
            form.errors.append(str(e))

    return render_template('verseny/edit.html', form=form, format_epoch=format_epoch, feladatok=feladatok)


@bp.route('/edit/<verseny_id>', methods=('get', 'post'))
@has_role('ZSURI')
def edit_verseny(verseny_id):
    verseny = Verseny.find_by_id(verseny_id) or abort(404)
    feladatok = Feladat.find_all()
    form = VersenyForm(
        name=verseny.name,
        description=verseny.description,
        kezdet=verseny.kezdet,
        veg=verseny.veg,
        evfolyam=verseny.evfolyam,
        feladatok=Feladat.find_by_verseny(verseny_id)
    )

    if form.validate_on_submit():
        try:
            verseny.name = form.name,
            verseny.description = form.description,
            verseny.kezdet = form.kezdet,
            verseny.veg = form.veg,
            verseny.evfolyam = form.evfolyam

            Verseny.save(verseny)
            Verseny.remove_feladat(verseny)
            for sel in form.feladatok:
                Feladat.add_to_verseny(sel, verseny.id)

            flash('Verseny elmentve.')

            return redirect(url_for('verseny.verseny_list'))
        except IntegrityError as e:
            form.errors.append(str(e))

    return render_template('verseny/edit.html', form=form, format_epoch=format_epoch, feladatok=feladatok)


@bp.route('/delete/<verseny_id>', methods=('post',))
@has_role('ZSURI')
def delete_verseny(verseny_id):
    verseny = Verseny.find_by_id(verseny_id) or abort(404)

    try:
        Verseny.delete(verseny.id)
        flash('Verseny törölve.')
    except IntegrityError as e:
        flash(str(e))

    return redirect(url_for('verseny.verseny_list'))


@bp.route('/result/<verseny_id>')
@has_role('ZSURI')
def result(verseny_id):
    verseny = Verseny.find_by_id(verseny_id) or abort(404)
    teams = Team.find_by_verseny(verseny_id)
    users = []
    for team in teams:
        curus = User.find_by_team(team.id)
        users.append(curus)
        team.pont = 0
        for user in curus:
            team.pont += user.helyes

    teams = sorted(teams, key=lambda x: x.pont, reverse=True)

    for i in range(len(teams)):
        teams[i].helyezes = i+1
        if i > 0 and teams[i-1].pont == teams[i].pont:
            teams[i].helyezes = teams[i-1].helyezes

    return render_template('verseny/result.html', teams=teams, users=users)
