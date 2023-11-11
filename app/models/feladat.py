import random

from app.connection import execute, fetchone, fetchall
from app.models.user import User


class Feladat:
    def __init__(self, strings, number, id=None, upload_id=None, _upload=None):
        self.id = id
        self.upload_id = upload_id
        self._upload = _upload
        self.strings = strings
        self.number = number

    def scramble(self):
        char_list = list(self.strings[3])
        random.shuffle(char_list)
        self.strings[3] = ''.join(char_list)

    @property
    def upload(self):
        if self._upload is None and self.upload_id:
            self._upload = Upload.find_by_id(self.upload_id)

        return self._upload

    @upload.setter
    def upload(self, _upload):
        self._upload = _upload
        self.upload_id = _upload.id

    @staticmethod
    def create_from_row(row):
        return Feladat(id=row['id'], upload_id=row['upload_id'], strings=row['data'].split(), number=row['number'])

    @staticmethod
    def save(feladat):
        query = '''
        INSERT INTO `feladat`(`data`, `number`, `upload_id`)
        VALUES (%s, %s, %s);
        '''

        feladat.id = execute(query, (' '.join(feladat.strings), feladat.number, feladat.upload.id))

    @staticmethod
    def find_in_range(start, end):
        query = '''
        SELECT `id`,`data`,`number`,`upload_id` FROM `feladat` ORDER BY `id` LIMIT %s OFFSET %s;
        '''

        return [Feladat.create_from_row(row) for row in fetchall(query, (end - start, start))]

    @staticmethod
    def get_by_id(id):
        query = '''
        SELECT `id`, `data`, `number`, `upload_id` FROM `feladat` WHERE `id` = %s;
        '''

        return Feladat.create_from_row(fetchone(query, (id,)))


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