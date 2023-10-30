from flask import request


class UserForm:
    def __init__(self, username='', password='', role_id=0, create=False):
        self.username = username
        self.password = password
        self.role_id = role_id
        self.create = create
        self.errors = []

    def validate_on_submit(self):
        if request.method != 'POST':
            return False

        self.username = request.form.get('username', '').strip()
        self.password = request.form.get('password', '')
        self.role_id = int(request.form.get('role_id', '0'))
        self.errors = []

        if self.username == '':
            self.errors.append('Username missing.')

        if self.create and self.password == '':
            self.errors.append('Password missing.')

        return len(self.errors) == 0
