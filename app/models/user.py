from werkzeug.security import generate_password_hash, check_password_hash

from app.connection import fetchall, fetchone, execute
from app.models.team import Team


class User:
    def __init__(self, username, digest=None, role_id=None, user_id=None, evfolyam=5, osztaly='', team_id=None, progress=0, helyes=0, password=None, _team=None):
        self.user_id = user_id
        self.username = username
        self.digest = digest
        self.role_id = role_id
        self.password = password
        self.evfolyam = evfolyam
        self.osztaly = osztaly
        self._team_id = team_id
        self.progress = progress
        self.helyes = helyes
        self._team = _team

    @property
    def password(self):
        return None

    @password.setter
    def password(self, value):
        if value and len(value) > 0:
            self.digest = generate_password_hash(value)

    @property
    def team(self):
        if self._team is None and self._team_id:
            self._team = Team.find_by_id(self._team_id)

        return self._team

    @team.setter
    def team(self, team):
        self._team = team
        self._team_id = team.id

    @property
    def team_id(self):
        return self._team_id

    @team_id.setter
    def team_id(self, team_id):
        self._team_id = team_id
        self._team = None

    @property
    def role(self):
        return Role.find_by_id(self.role_id)

    def check_password(self, password):
        return check_password_hash(self.digest, password)

    @staticmethod
    def create_from_row(row):
        if row is None:
            return None

        return User(row['username'], row['digest'], row['role_id'], row['id'], row['evfolyam'], row['osztaly'],
                    row['team_id'], row['helyes'], row['progress'])

    @staticmethod
    def find_all():
        query = '''
            SELECT `id`, `username`, `digest`, `role_id`, `evfolyam`, `osztaly`, `team_id`, `helyes`, `progress`
            FROM `users`
            ORDER BY `username`;
        '''

        return [User.create_from_row(row) for row in fetchall(query)]

    @staticmethod
    def find_by_id(user_id):
        query = '''
            SELECT `id`, `username`, `digest`, `role_id`, `evfolyam`, `osztaly`, `team_id`, `helyes`, `progress`
            FROM `users`
            WHERE `id` = %s;
        '''

        return User.create_from_row(fetchone(query, (user_id,)))

    @staticmethod
    def find_by_username(username):
        query = '''
            SELECT `id`, `username`, `digest`, `role_id`, `evfolyam`, `osztaly`, `team_id`, `helyes`, `progress`
            FROM `users`
            WHERE `username` = %s;
        '''

        return User.create_from_row(fetchone(query, (username,)))

    @staticmethod
    def find_by_role_id(role_id):
        query = '''
                SELECT `id`, `username`, `digest`, `role_id`, `evfolyam`, `osztaly`, `team_id`, `helyes`, `progress`
                FROM `users`
                WHERE `role_id` = %s
                ORDER BY `username`;
            '''

        return [User.create_from_row(row) for row in fetchall(query, (role_id,))]

    @staticmethod
    def find_by_username_and_role_id(username, role_id):
        query = '''
                SELECT `id`, `username`, `digest`, `role_id`, `evfolyam`, `osztaly`, `team_id`, `helyes`, `progress`
                FROM `users`
                WHERE `username` = %s AND `role_id` = %s;
            '''

        return User.create_from_row(fetchone(query, (username, role_id)))

    @staticmethod
    def find_by_team(team_id):
        query = '''
                SELECT `id`, `username`, `digest`, `role_id`, `evfolyam`, `osztaly`, `team_id`, `helyes`, `progress`
                FROM `users`
                WHERE `team_id` = %s;
        '''

        return [User.create_from_row(row) for row in fetchall(query, (team_id,))]

    @staticmethod
    def find_by_evfolyam(evfolyam):
        query = '''
                SELECT `id`, `username`, `digest`, `role_id`, `evfolyam`, `osztaly`, `team_id`, `helyes`, `progress`
                FROM `users`
                WHERE `evfolyam` = %s;
        '''

        return [User.create_from_row(row) for row in fetchall(query, (evfolyam,))]

    @staticmethod
    def save(user):
        if user.user_id:
            query = '''
                    UPDATE `users`
                    SET `username` = %s,
                        `digest` = %s,
                        `role_id` = %s, `evfolyam` = %s, `osztaly` = %s, `team_id` = %s, `helyes` = %s, `progress` = %s
                    WHERE `id` = %s;
                '''

            execute(query, (user.username, user.digest, user.role_id, user.evfolyam, user.osztaly, user.team_id,
                            user.helyes, user.progress, user.user_id))
        else:
            query = '''
                    INSERT INTO `users`(`username`, `digest`, `role_id`, `evfolyam`, `osztaly`, `team_id`, `helyes`, `progress`)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                '''

            user.user_id = execute(query, (user.username, user.digest, user.role_id, user.evfolyam, user.osztaly,
                                           user.team_id, user.helyes, user.progress))

        return user

    @staticmethod
    def delete(user_id):
        query = '''
                DELETE FROM `users`
                WHERE `id` = %s;
            '''

        execute(query, (user_id,))


from app.models.role import Role
