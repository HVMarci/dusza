from flask import request

from app.models.role import Role


class UserForm:
    def __init__(self, username='', password='', evfolyam=5, osztaly='', role_id=0, create=False):
        self.username = username
        self.password = password
        self.evfolyam = evfolyam
        self.osztaly = osztaly
        self.role_id = role_id
        self.create = create
        self.errors = []

    def validate_on_submit(self):
        if request.method != 'POST':
            return False

        self.username = request.form.get('username', '').strip()
        self.password = request.form.get('password', '')
        self.role_id = int(request.form.get('role_id', '0'))
        self.evfolyam = int(request.form.get('evfolyam', '0'))
        self.osztaly = request.form.get('osztaly', '')
        self.errors = []

        if self.username == '':
            self.errors.append('Hiányzik a felhasználónév.')

        if self.create and self.password == '':
            self.errors.append('Hiányzik a jelszó.')

        if self.role_id == Role.find_by_name("DIAK").role_id:
            if self.osztaly == '':
                self.errors.append('Hiányzik az évfolyam vagy az osztály.')

        return len(self.errors) == 0
