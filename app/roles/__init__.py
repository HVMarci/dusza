from flask import Blueprint

bp = Blueprint('roles', __name__)

from app.roles import routes
