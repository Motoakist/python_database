from flask import Flask
from .database import init_db
from .config import Config
from . import models

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)

    return app

app = create_app()