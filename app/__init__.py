import os

from pathlib import Path

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from dotenv import load_dotenv

basedir = Path(__file__).resolve().parent.parent
load_dotenv(basedir.joinpath('.env'))

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    db.init_app(app)
    migrate.init_app(app, db)

    return app
