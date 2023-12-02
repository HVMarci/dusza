import datetime
from time import time

from flask import request

from app.models.feladat import Feladat
from app.models.user import User


class VersenyForm:
    def __init__(self, name='', description='', kezdet=time(), veg=time(), evfolyam=5, feladatok=[], create=False):
        self.name = name
        self.description = description
        self.kezdet = kezdet
        self.veg = veg
        self.evfolyam = evfolyam
        self.create = create
        self.feladatok = feladatok
        self.errors = []

    def validate_on_submit(self):
        if request.method != 'POST':
            return False

        self.name = request.form.get('name', '').strip()
        self.description = request.form.get('description', '').strip()
        try:
            self.evfolyam = int(request.form.get('evfolyam', 5))
        except ValueError as e:
            self.errors.append('Hibás az évfolyam.')
        self.feladatok = [int(sel[3:]) for sel, val in request.form.items() if sel.startswith('sel') and val == 'on' and
                          Feladat.find_by_id(int(sel[3:])).number == self.evfolyam]

        kezdet_string = request.form.get('kezdet', '').strip()
        if len(kezdet_string) > 16:  # includes seconds
            format_string = "%Y-%m-%dT%H:%M:%S"
        else:  # does not include seconds
            format_string = "%Y-%m-%dT%H:%M"
        self.kezdet = (datetime.datetime.strptime(kezdet_string, format_string).timestamp())

        veg_string = request.form.get('veg', '').strip()
        if len(veg_string) > 16:  # includes seconds
            format_string = "%Y-%m-%dT%H:%M:%S"
        else:  # does not include seconds
            format_string = "%Y-%m-%dT%H:%M"

        self.veg = datetime.datetime.strptime(veg_string, format_string).timestamp()
        try:
            self.evfolyam = int(request.form.get('evfolyam', '0'))
        except ValueError as e:
            self.errors.append('Hibás az évfolyam.')

        if self.name == '':
            self.errors.append('Hiányzik a név.')

        if self.description == '':
            self.errors.append('Hiányzik a leírás.')

        if self.evfolyam < 5 or self.evfolyam > 8:
            self.errors.append('Hibás az évfolyam.')

        if self.kezdet >= self.veg:
            self.errors.append('A verseny a vége után kezdődik.')

        if len(self.feladatok) == 0 or len(self.feladatok) % 3 != 0:
            self.errors.append('Nincs kiválasztva feladat, vagy számuk nem hárommal osztható!')

        return len(self.errors) == 0

