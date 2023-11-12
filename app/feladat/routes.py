from flask import render_template, g, redirect, flash, url_for, abort
from pymysql import IntegrityError

from app.feladat import bp
from app.feladat.forms import UploadForm, EditForm
from app.models.feladat import Feladat, Upload
from app.security import has_role


def process_line(line):
    parts = line.split()

    if len(parts) != 5:
        return False

    try:
        number = int(parts[4])
        if number < 5 or number > 8:
            return False
    except ValueError:
        return False

    return [b.decode('utf-8') for b in parts[0:4]], number


@bp.route('/')
@has_role('TANAR')
def feladat_list():
    feladatok = Feladat.find_all()

    return render_template('feladat/list.html', feladatok=feladatok)


@bp.route('/upload', methods=('post', 'get'))
@has_role('TANAR')
def feladat_upload():
    form = UploadForm()

    if form.validate_on_submit():
        try:
            feladatok = []

            for line in form.file:
                result = process_line(line)
                if result:
                    feladatok.append(Feladat(result[0], result[1]))

            if len(feladatok) > 0:
                upload = Upload(g.user.user_id)
                Upload.save(upload)

                for feladat in feladatok:
                    feladat.upload = upload
                    Feladat.save(feladat)

                flash('Feladat feltöltve.')
                return redirect(url_for('feladat.feladat_list'))
            else:
                form.errors.append('Nincs helyes feladat a fájlban!')

        except IntegrityError as e:
            form.errors.append(str(e))

    return render_template('feladat/upload.html', form=form)


@bp.route('/edit/<feladat_id>', methods=('get', 'post'))
@has_role('TANAR')
def edit_feladat(feladat_id):
    feladat = Feladat.find_by_id(feladat_id) or abort(404)
    if feladat.upload.user_id != g.user.user_id:
        abort(403)

    form = EditForm(
        szo1=feladat.strings[0],
        szo2=feladat.strings[1],
        szo3=feladat.strings[2],
        szo4=feladat.strings[3],
        evfolyam=feladat.number
    )

    if form.validate_on_submit():
        try:
            feladat.strings = (form.szo1, form.szo2, form.szo3, form.szo4)
            feladat.number = form.evfolyam

            Feladat.save(feladat)

            flash('Feladat elmentve.')

            return redirect(url_for('feladat.feladat_list'))
        except IntegrityError as e:
            form.errors.append(str(e))

    return render_template('feladat/edit.html', form=form)


@bp.route('/delete/<feladat_id>', methods=('post',))
@has_role('TANAR')
def delete_feladat(feladat_id):
    feladat = Feladat.find_by_id(feladat_id) or abort(404)

    try:
        Feladat.delete(feladat.id)
        flash('Feladat törölve.')
    except IntegrityError as e:
        flash(str(e))

    return redirect(url_for('feladat.feladat_list'))

