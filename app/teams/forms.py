from flask import request

from app.models.user import User


class TeamForm:
    def __init__(self, team_name='', description='', user_ids=(0,0,0), evfolyam=5, osztaly='', verseny_id=0, create=False):
        self.team_name = team_name
        self.description = description
        self.user_ids = user_ids
        self.evfolyam = evfolyam
        self.osztaly = osztaly
        self.create = create
        self.verseny_id = verseny_id
        self.errors = []

    def validate_on_submit(self):
        if request.method != 'POST':
            return False

        self.team_name = request.form.get('team_name', '').strip()
        self.description = request.form.get('description', '').strip()
        self.evfolyam = int(request.form.get('evfolyam', '0'))
        self.osztaly = request.form.get('osztaly', '').strip()
        self.verseny_id = int(request.form.get('verseny_id').strip())

        if self.team_name == '':
            self.errors.append('Hiányzik a csapatnév.')

        if self.description == '':
            self.errors.append('Hiányzik a leírás.')

        if len(self.osztaly) != 1:
            self.errors.append('Az osztály hibás.')

        if self.evfolyam < 5 or self.evfolyam > 8:
            self.errors.append('Az évfolyam hibás.')

        try:
            self.user_ids = ()
            users = []
            for i in range(3):
                self.user_ids += (int(request.form.get(f'diak{i}').strip()),)
                users.append(User.find_by_id(self.user_ids[i]))
                if not users[i] or users[i].osztaly != self.osztaly or users[i].evfolyam != self.evfolyam:
                    self.errors.append(f'Hibás felhasználó: {users[i].username}')

            if len(self.user_ids) != len(set(self.user_ids)):
                self.errors.append('Ismétlődő felhasználó!')

        except Exception as e:
            self.errors.append('Nincs elég felhasználó kiválasztva.')

        return len(self.errors) == 0

