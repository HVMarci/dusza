from random import random, randint

from app.models.feladat import Feladat
from app.models.verseny import Verseny
from app.verseny import bp

from flask import render_template, flash, redirect, url_for, abort
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
    versenyek = Verseny.get_all()

    return render_template('verseny/list.html', versenyek=versenyek, time=time, format_epoch=format_epoch)


@bp.route('/play/<id>', methods=('get', 'post'))
@has_role('DIAK')
def verseny_play(id):
    feladat = Feladat.get_by_id(randint(1,4))
    feladat.scramble()

    return render_template('verseny/play.html', feladat=feladat)
