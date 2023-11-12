from random import random, randint

from app.models.feladat import Feladat
from app.models.verseny import Verseny
from app.verseny import bp

from flask import render_template, flash, redirect, url_for, abort, g, request
from pymysql import IntegrityError

from app.models.role import Role
from app.models.user import User
from app.roles.forms import RoleForm, RoleUserForm
from app.security import has_role
from time import time
from datetime import datetime


def format_epoch(epoch_time):
    return datetime.fromtimestamp(epoch_time).strftime("%Y-%m-%d %H:%M:%S")


@bp.route('/')
@has_role('DIAK')
def verseny_list():
    versenyek = []

    if g.user.team_id and g.user.team.verseny_id:
        versenyek.append(Verseny.find_by_id(g.user.team.verseny_id))

    return render_template('verseny/list.html', versenyek=versenyek, time=time, format_epoch=format_epoch)


@bp.route('/play/<id>', methods=('get', 'post'))
@has_role('DIAK')
def verseny_play(id):
    feladat, hossz = Feladat.get_by_progress(g.user.progress, g.user.team.verseny_id)

    if request.method == 'POST':
        if request.get_data('megoldas'):
            g.user.helyes += 1
        g.user.progress += 1
        User.save(g.user)

    if g.user.progress == hossz+1:
        flash('Vége a versenynek!')
        return redirect(url_for('verseny.list_verseny'))

    return render_template('verseny/play.html', feladat=feladat)
