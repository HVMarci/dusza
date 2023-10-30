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

    from app.roles import bp as roles_bp
    app.register_blueprint(roles_bp, url_prefix='/roles')

    from app.users import bp as users_bp
    app.register_blueprint(users_bp, url_prefix='/users')

    return app
