import click
import pymysql
import pymysql.cursors
from flask import g, current_app
from pymysql.constants import CLIENT


def get_connection():
    if 'connection' not in g:
        g.connection = pymysql.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USERNAME'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_DATABASE'],
            cursorclass=pymysql.cursors.DictCursor
        )

    return g.connection


def execute(query, args=None):
    with get_connection().cursor() as cursor:
        cursor.execute(query, args)
        lastrowid = cursor.lastrowid

    get_connection().commit()

    return lastrowid


def fetchone(query, args=None):
    with get_connection().cursor() as cursor:
        cursor.execute(query, args)

        return cursor.fetchone()


def fetchall(query, args=None):
    with get_connection().cursor() as cursor:
        cursor.execute(query, args)

        return cursor.fetchall()


def init_app(app):
    app.teardown_appcontext(__close_connection)
    app.cli.add_command(__migrate_command)


def __close_connection(e=None):
    connection = g.pop('connection', None)

    if connection is not None:
        connection.close()


@click.command('migrate')
def __migrate_command():
    __migrate()
    click.echo('Database migration successful.')


def __migrate():
    connection = pymysql.connect(
        host=current_app.config['DB_HOST'],
        user=current_app.config['DB_USERNAME'],
        password=current_app.config['DB_PASSWORD'],
        database=current_app.config['DB_DATABASE'],
        cursorclass=pymysql.cursors.DictCursor,
        client_flag=CLIENT.MULTI_STATEMENTS
    )

    with connection:
        with connection.cursor() as cursor:
            with current_app.open_resource('migration.sql') as file:
                cursor.execute(file.read().decode('utf8'))

        connection.commit()
