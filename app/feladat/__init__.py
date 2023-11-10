from flask import Blueprint

bp = Blueprint('feladat', __name__)

from app.feladat import routes
