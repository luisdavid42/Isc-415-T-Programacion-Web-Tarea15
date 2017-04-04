
class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = "sqlite://:memory:"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db/app.db"
    SQLALCHEMY_MIGRATE_REPO = "sqlite:///db/db_repo/"


