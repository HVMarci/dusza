from app.connection import fetchall, fetchone


class Verseny:
    def __init__(self, kezdet, veg, id=None):
        self.id = id
        self.kezdet = kezdet
        self.veg = veg

    @staticmethod
    def create_from_row(row):
        return Verseny(row['kezdet'], row['veg'], row['id'])

    @staticmethod
    def find_all():
        query = '''
        SELECT `id`, `kezdet`, `veg` FROM `verseny`;
        '''

        return [Verseny.create_from_row(row) for row in fetchall(query)]

    @staticmethod
    def find_by_id(id):
        query = '''
        SELECT `id`, `kezdet`, `veg` FROM `verseny`
        WHERE `id` = %s;
        '''

        return Verseny.create_from_row(fetchone(query, (id,)))
