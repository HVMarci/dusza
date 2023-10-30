from werkzeug.security import generate_password_hash, check_password_hash

from app.connection import fetchall, fetchone, execute


class User:
    def __init__(self, username, digest=None, role_id=None, user_id=None, password=None, ):
        self.user_id = user_id
        self.username = username
        self.digest = digest
        self.role_id = role_id
        self.password = password

    @property
    def password(self):
        return None

    @password.setter
    def password(self, value):
        if value and len(value) > 0:
            self.digest = generate_password_hash(value)

    @property
    def role(self):
        return Role.find_by_id(self.role_id)

    def check_password(self, password):
        return check_password_hash(self.digest, password)

    @staticmethod
    def create_from_row(row):
        if row is None:
            return None

        return User(row['username'], row['digest'], row['role_id'], row['id'])

    @staticmethod
    def find_all():
        query = '''
            SELECT `id`, `username`, `digest`, `role_id`
            FROM `users`
            ORDER BY `username`;
        '''

        return [User.create_from_row(row) for row in fetchall(query)]

    @staticmethod
    def find_by_id(user_id):
        query = '''
            SELECT `id`, `username`, `digest`, `role_id`
            FROM `users`
            WHERE `id` = %s;
        '''

        return User.create_from_row(fetchone(query, (user_id,)))

    @staticmethod
    def find_by_username(username):
        query = '''
            SELECT `id`, `username`, `digest`, `role_id`
            FROM `users`
            WHERE `username` = %s;
        '''

        return User.create_from_row(fetchone(query, (username,)))

    @staticmethod
    def find_by_role_id(role_id):
        query = '''
                SELECT `id`, `username`, `digest`, `role_id`
                FROM `users`
                WHERE `role_id` = %s
                ORDER BY `username`;
            '''

        return [User.create_from_row(row) for row in fetchall(query, (role_id,))]

    @staticmethod
    def find_by_username_and_role_id(username, role_id):
        query = '''
                SELECT `id`, `username`, `digest`, `role_id`
                FROM `users`
                WHERE `username` = %s AND `role_id` = %s;
            '''

        return User.create_from_row(fetchone(query, (username, role_id)))

    @staticmethod
    def save(user):
        if user.user_id:
            query = '''
                    UPDATE `users`
                    SET `username` = %s,
                        `digest` = %s,
                        `role_id` = %s
                    WHERE `id` = %s;
                '''

            execute(query, (user.username, user.digest, user.role_id, user.user_id))
        else:
            query = '''
                    INSERT INTO `users`(`username`, `digest`, `role_id`)
                    VALUES (%s, %s, %s);
                '''

            user.user_id = execute(query, (user.username, user.digest, user.role_id))

        return user

    @staticmethod
    def delete(user_id):
        query = '''
                DELETE FROM `users`
                WHERE `id` = %s;
            '''

        execute(query, (user_id,))


from app.models.role import Role
