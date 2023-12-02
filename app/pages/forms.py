from flask import request


class LoginForm:
    def __init__(self, username='', password=''):
        self.username = username
        self.password = password
        self.errors = []

    def validate_on_submit(self):
        if request.method != 'POST':
            return False

        self.username = request.form.get('username', '').strip()
        self.password = request.form.get('password', '')
        self.errors = []

        if self.username == '':
            self.errors.append('Hiányzik a felhasználónév.')

        if self.password == '':
            self.errors.append('Hiányzik a jelszó.')

        return len(self.errors) == 0
