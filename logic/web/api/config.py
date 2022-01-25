import os

basedir = os.path.abspath( os.path.dirname(__file__) )

class Config(object):

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URL = os.environ("DATABASE_URL", 'sqlite://')