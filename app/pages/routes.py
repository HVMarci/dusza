import os
from urllib.parse import urlsplit

from flask import render_template, g, redirect, url_for, session, flash, request, abort, send_from_directory
from pymysql import IntegrityError
from werkzeug.utils import secure_filename

from app import create_app
from app.models.homepage import Homepage
from app.models.user import User
from app.pages import bp
from app.pages.forms import LoginForm, HomepageForm
from app.security import is_fully_authenticated, has_role


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if g.user is not None:
        return redirect(url_for('pages.home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.find_by_username(form.username)

        if user is not None and user.check_password(form.password):
            session['user_id'] = user.user_id
            flash('Sikeres bejelentkezés.')

            if request.args.get('redirect') is not None \
                    and urlsplit(request.args.get('redirect')).netloc == '':
                return redirect(request.args.get('redirect'))

            return redirect(url_for('pages.home'))
        else:
            form.errors.append('Hibás felhasználónév vagy jelszó.')

    return render_template('pages/login.html', form=form)


@bp.route('/logout')
def logout():
    session.clear()
    flash('Sikeres kijelentkezés.')

    return redirect(url_for('pages.home'))


@bp.route('/')
def home():
    hp = Homepage.find_last()
    return render_template('pages/home.html', content=hp.data)


@bp.route('/bemutatkozas')
@is_fully_authenticated
def bemutatkozas():
    return render_template('pages/bemutatkozas.html')


@bp.route('/edit_homepage', methods=('get', 'post'))
@has_role('ADMIN')
def edit_homepage():
    form = HomepageForm()

    if form.validate_on_submit():
        try:
            hp = Homepage(form.data)
            Homepage.save(hp)
            flash('Főoldal módosítva.')

            return redirect(url_for('pages.home'))
        except IntegrityError as e:
            form.errors.append(str(e))

    hp = Homepage.find_last()
    form.data = hp.data

    return render_template('pages/edit_homepage.html', form=form)


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@bp.route('/upload_image', methods=('post',))
@has_role('ADMIN')
def upload_image():
    app = create_app()
    if request.method == 'POST':
        if 'file' not in request.files:
            abort(400)
        file = request.files['file']

        if file.filename == '':
            abort(400)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(os.path.join('static/uploaded_images', filename))

    abort(400)
