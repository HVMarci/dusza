from app.connection import fetchall


class Verseny:
    def __init__(self, kezdet, veg, id=None):
        self.id = id
        self.kezdet = kezdet
        self.veg = veg

    @staticmethod
    def create_from_row(row):
        return Verseny(row['kezdet'], row['veg'], row['id'])

    @staticmethod
    def get_all():
        query = '''
        SELECT `id`, `kezdet`, `veg` FROM `verseny`
        '''

        return [Verseny.create_from_row(row) for row in fetchall(query)]

