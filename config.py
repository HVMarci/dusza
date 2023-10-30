import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_USERNAME = os.environ.get('DB_USERNAME') or 'root'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'password'
    DB_DATABASE = os.environ.get('DB_DATABASE') or 'flask-starter'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
