from urllib.parse import urlsplit

from flask import render_template, g, redirect, url_for, session, flash, request

from app.models.user import User
from app.pages import bp
from app.pages.forms import LoginForm


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
    flash('Logout successful.')

    return redirect(url_for('pages.home'))


@bp.route('/')
def home():
    return render_template('pages/home.html')
