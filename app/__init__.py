from flask import Flask

from app import connection, security
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    connection.init_app(app)
    security.init_app(app)

    from app.pages import bp as pages_bp
    app.register_blueprint(pages_bp, url_prefix='/')

    #from app.roles import bp as roles_bp
    #app.register_blueprint(roles_bp, url_prefix='/roles')

    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    from app.feladat import bp as feladat_bp
    app.register_blueprint(feladat_bp, url_prefix='/feladat')

    from app.verseny import bp as verseny_bp
    app.register_blueprint(verseny_bp, url_prefix='/verseny')

    from app.teams import bp as teams_bp
    app.register_blueprint(teams_bp, url_prefix='/teams')

    return app
