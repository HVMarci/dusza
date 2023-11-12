import random

from app.connection import execute, fetchone, fetchall
from app.models.user import User


class Feladat:
    def __init__(self, strings, number, id=None, upload_id=None, upload=None):
        self.id = id
        self._upload_id = upload_id
        self._upload = upload
        self.strings = strings
        self.number = number
        self.scrambled = self.strings[3]
        if self.id:
            i = self.id + 123456
            while self.scrambled == self.strings[3]:
                scrambled = bytearray(strings[3].encode('utf-8'))
                random.seed(i)
                random.shuffle(scrambled)
                self.scrambled = ''.join(scrambled.decode('utf-8'))
                i += 1

    @property
    def upload(self):
        if self._upload is None and self._upload_id:
            self._upload = Upload.find_by_id(self._upload_id)

        return self._upload

    @upload.setter
    def upload(self, upload):
        self._upload = upload
        self._upload_id = upload.id

    @property
    def upload_id(self):
        return self._upload_id

    @upload_id.setter
    def upload_id(self, upload_id):
        self._upload_id = upload_id
        self._upload = None

    @staticmethod
    def create_from_row(row):
        return Feladat(id=row['id'], upload_id=row['upload_id'], strings=row['data'].split(), number=row['number'])

    @staticmethod
    def save(feladat):
        if feladat.id:
            query = '''
                    UPDATE `feladat`
                    SET `data` = %s,
                        `number` = %s,
                        `upload_id` = %s
                    WHERE `id` = %s;
                '''

            execute(query, (' '.join(feladat.strings), feladat.number, feladat.upload_id, feladat.id))
        else:
            query = '''
            INSERT INTO `feladat`(`data`, `number`, `upload_id`)
            VALUES (%s, %s, %s);
            '''

            feladat.id = execute(query, (' '.join(feladat.strings), feladat.number, feladat.upload.id))

        return feladat

    @staticmethod
    def add_to_verseny(feladat_id, verseny_id):
        query ='''
        INSERT INTO `verseny_feladat`(`verseny_id`, `feladat_id`)
        VALUES (%s, %s);
        '''

        execute(query, (verseny_id, feladat_id))

    @staticmethod
    def find_by_verseny(verseny_id):
        query = '''
        SELECT `feladat_id` FROM `verseny_feladat` WHERE `verseny_id` = %s;
        '''

        return [row['feladat_id'] for row in fetchall(query, (verseny_id,))]

    @staticmethod
    def find_all():
        query = '''
        SELECT `id`,`data`,`number`,`upload_id` FROM `feladat` ORDER BY `id`;
        '''

        return [Feladat.create_from_row(row) for row in fetchall(query)]

    @staticmethod
    def find_by_id(id):
        query = '''
        SELECT `id`, `data`, `number`, `upload_id` FROM `feladat` WHERE `id` = %s;
        '''

        return Feladat.create_from_row(fetchone(query, (id,)))

    @staticmethod
    def find_by_progress(progress, verseny_id):
        query = '''
        SELECT `verseny_id`, `feladat_id` FROM `verseny_feladat` WHERE `verseny_id` = %s ORDER BY `feladat_id`;
        '''

        rows = fetchall(query, (verseny_id,))

        if progress >= len(rows):
            return None, len(rows)

        return Feladat.find_by_id(rows[progress]['feladat_id']), len(rows)

    @staticmethod
    def delete(id):
        query = '''
                DELETE FROM `feladat`
                WHERE `id` = %s;
            '''

        execute(query, (id,))


class Upload:
    def __init__(self, user_id, id=None, _user=None):
        self._user = _user
        self.id = id
        self.user_id = user_id

    @property
    def user(self):
        if self._user is None and self.user_id:
            self._user = User.find_by_id(self.user_id)

        return self._user

    @user.setter
    def user(self, _user):
        self._user = _user
        self.user_id = _user.id

    @staticmethod
    def save(upload):
        query = '''
        INSERT INTO `upload`(`user_id`)
        VALUES (%s);
        '''

        upload.id = execute(query, (upload.user.user_id,))

    @staticmethod
    def create_from_row(row):
        if row is None:
            return None

        return Upload(row['user_id'])

    @staticmethod
    def find_by_id(id):
        query = '''
        SELECT `user_id` FROM `upload` WHERE `id` = %s;
        '''

        return Upload.create_from_row(fetchone(query, (id,)))
