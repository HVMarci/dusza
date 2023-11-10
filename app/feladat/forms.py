from flask import request


class UploadForm:
    def __init__(self, file=''):
        self.file = file
        self.errors = []

    def validate_on_submit(self):
        if request.method != 'POST':
            return False

        self.errors = []

        if 'file' not in request.files:
            self.errors.append('Nincs feltöltve fájl!')
            return False

        self.file = request.files['file']
        if self.file.filename == '':
            self.errors.append('Nincs feltölve fájl2!')
            return False

        return len(self.errors) == 0
