from app.connection import fetchall, fetchone, execute


class Verseny:
    def __init__(self, name, description, kezdet, veg, evfolyam, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.kezdet = kezdet
        self.veg = veg
        self.evfolyam = evfolyam

    @staticmethod
    def create_from_row(row):
        return Verseny(row['name'], row['description'], row['kezdet'], row['veg'], row['evfolyam'], row['id'])

    @staticmethod
    def find_all():
        query = '''
        SELECT `id`, `name`, `description`, `kezdet`, `veg`, `evfolyam` FROM `verseny`;
        '''

        return [Verseny.create_from_row(row) for row in fetchall(query)]

    @staticmethod
    def find_by_id(id):
        query = '''
        SELECT `id`, `name`, `description`, `kezdet`, `veg`, `evfolyam` FROM `verseny`
        WHERE `id` = %s;
        '''

        return Verseny.create_from_row(fetchone(query, (id,)))

    @staticmethod
    def save(verseny):
        if verseny.id:
            query = '''
                    UPDATE `verseny`
                    SET `name` = %s,
                        `description` = %s,
                        `kezdet` = %s, `veg` = %s, `evfolyam` = %s
                    WHERE `id` = %s;
                '''

            execute(query, (verseny.name, verseny.description, verseny.kezdet, verseny.veg, verseny.evfolyam,
                            verseny.id))
        else:
            query = '''
                    INSERT INTO `verseny`(`name`, `description`, `kezdet`, `veg`, `evfolyam`)
                    VALUES (%s, %s, %s, %s, %s);
                '''

            verseny.id = execute(query, (verseny.name, verseny.description, verseny.kezdet, verseny.veg,
                                         verseny.evfolyam))

        return verseny

    @staticmethod
    def delete(verseny_id):
        query = '''
                DELETE FROM `verseny`
                WHERE `id` = %s;
            '''

        execute(query, (verseny_id,))

    @staticmethod
    def remove_feladat(verseny):
        query = '''
        DELETE FROM `verseny_feladat`
        WHERE verseny_id = %s;
        '''

        execute(query, (verseny.id,))
