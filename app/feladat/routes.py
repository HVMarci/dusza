from flask import render_template, g, redirect, flash, url_for
from pymysql import IntegrityError

from app.feladat import bp
from app.feladat.forms import UploadForm
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
    feladatok = Feladat.find_in_range(0, 100)

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
