from flask import request


class TeamForm:
    def __init__(self, team_name='', description='', user_ids=(0,0,0), evfolyam=5, osztaly='', create=False):
        self.team_name = team_name
        self.description = description
        self.user_ids = user_ids
        self.evfolyam = evfolyam
        self.osztaly = osztaly
        self.create = create
        self.errors = []

    def validate_on_submit(self):
        if request.method != 'POST':
            return False

        self.team_name = request.form.get('team_name', '').strip()
        self.description = request.form.get('description', '').strip()
        self.evfolyam = int(request.form.get('evfolyam', '0'))
        self.osztaly = request.form.get('osztaly', '').strip()

        if self.team_name == '':
            self.errors.append('Hiányzik a csapatnév.')

        if self.description == '':
            self.errors.append('Hiányzik a leírás.')

        if len(self.osztaly) != 1:
            self.errors.append('Az osztály hibás.')

        if self.evfolyam < 5 or self.evfolyam > 8:
            self.errors.append('Az évfolyam hibás.')

        try:
            user_ids = ()
            for i in range(3):
                user_ids += (int(request.form.get(f'diak{i}').strip()),)

            if len(user_ids) != len(set(user_ids)):
                self.errors.append('Ismétlődő felhasználó!')

            if 0 in user_ids:
                self.errors.append('Hibás felhasználóválasztás.')
        except ValueError as e:
            self.errors.append('Nincs elég felhasználó kiválasztva.')

        return len(self.errors) == 0

