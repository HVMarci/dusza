from app.connection import fetchall, fetchone, execute


class Role:
    def __init__(self, name, display_name, role_id=None):
        self.role_id = role_id
        self.name = name
        self.display_name = display_name

    @property
    def users(self):
        return User.find_by_role_id(self.role_id)

    @staticmethod
    def create_from_row(row):
        if row is None:
            return None

        return Role(row['name'], row['display_name'], row['id'])

    @staticmethod
    def find_all():
        query = '''
            SELECT `id`, `name`, `display_name`
            FROM `roles`
            ORDER BY `display_name`;
        '''

        return [Role.create_from_row(row) for row in fetchall(query)]

    @staticmethod
    def find_by_id(role_id):
        query = '''
            SELECT *
            FROM `roles`
            WHERE `id` = %s;
        '''

        return Role.create_from_row(fetchone(query, (role_id,)))

    @staticmethod
    def find_by_name(name):
        query = '''
            SELECT `id`, `name`, `display_name`
            FROM `roles`
            WHERE `name` = %s;
        '''

        return Role.create_from_row(fetchone(query, (name,)))

    @staticmethod
    def save(role):
        if role.role_id:
            query = '''
                UPDATE `roles`
                SET `name` = %s
                WHERE `id` = %s;
            '''

            execute(query, (role.name, role.role_id))
        else:
            query = '''
                INSERT INTO `roles`(`name`)
                VALUES (%s);
            '''

            role.role_id = execute(query, (role.name,))

        return role

    @staticmethod
    def delete(role_id):
        query = '''
            DELETE FROM `roles`
            WHERE `id` = %s;
        '''

        execute(query, (role_id,))


from app.models.user import User
