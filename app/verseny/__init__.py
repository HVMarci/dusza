from flask import Blueprint

bp = Blueprint('verseny', __name__)

from app.verseny import routes
