import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    API_KEY = os.environ.get("API_KEY")
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASS")
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_NAME = os.environ.get("DB_NAME")
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASS}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        basedir, '../tests/test.db'
    )
