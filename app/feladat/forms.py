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


class EditForm:
    def __init__(self, szo1, szo2, szo3, szo4, evfolyam):
        self.szo1 = szo1
        self.szo2 = szo2
        self.szo3 = szo3
        self.szo4 = szo4
        self.evfolyam = evfolyam

    def validate_on_submit(self):
        if request.method != 'POST':
            return False

        self.errors = []

        self.szo1 = request.form.get('szo1').strip()
        self.szo2 = request.form.get('szo2').strip()
        self.szo3 = request.form.get('szo3').strip()
        self.szo4 = request.form.get('szo4').strip()
        self.evfolyam = int(request.form.get('evfolyam'))

        if (len(self.szo4) < 3):
            self.errors.append('A 4. szónak legalább 3 betű hosszúnak kell lennie!')

        if self.evfolyam < 5 or self.evfolyam > 8:
            self.errors.append('Az évfolyam hibás.')

        return len(self.errors) == 0
