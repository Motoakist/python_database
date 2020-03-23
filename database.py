# initialization to use SQLAlchemy in Flask application
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# creating an object of class SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    Migrate(app, db)

    return db