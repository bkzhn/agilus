from os import environ

from dotenv import load_dotenv

load_dotenv()

class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
