from flask import request


class RoleForm:
    def __init__(self, name='', create=False):
        self.name = name
        self.create = create
        self.errors = []

    def validate_on_submit(self):
        if request.method != 'POST':
            return False

        self.name = request.form.get('name', '').strip().upper()
        self.errors = []

        if self.name == '':
            self.errors.append('Name missing.')

        return len(self.errors) == 0


class RoleUserForm:
    def __init__(self, username='', password='', create=False):
        self.username = username
        self.password = password
        self.create = create
        self.errors = []

    def validate_on_submit(self):
        if request.method != 'POST':
            return False

        self.username = request.form.get('username', '').strip()
        self.password = request.form.get('password', '')
        self.errors = []

        if self.username == '':
            self.errors.append('Username missing.')

        if self.create and self.password == '':
            self.errors.append('Password missing.')

        return len(self.errors) == 0
