from app.connection import fetchall, fetchone, execute


class Homepage:
    def __init__(self, data='', id=0):
        self.data = data
        self.id = id

    @staticmethod
    def create_from_row(row):
        return Homepage(row['data'], row['id'])

    @staticmethod
    def find_last():
        query = '''
                SELECT `id`, `data`
                FROM `homepage`
                ORDER BY `id` DESC
                LIMIT 1;
            '''

        return Homepage.create_from_row(fetchone(query))

    @staticmethod
    def save(hp):
        query = '''
            INSERT INTO `homepage`(`data`)
            VALUES (%s);
        '''

        return execute(query, hp.data)
