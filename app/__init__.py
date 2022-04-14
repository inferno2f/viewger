import os

from pathlib import Path

from flask_migrate import Migrate
from flask import Flask
from dotenv import load_dotenv

basedir = Path(__file__).resolve().parent.parent
load_dotenv(basedir.joinpath('.env'))

migrate = Migrate()


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    from .db import db
    db.init_app(app)

    from app import views
    app.register_blueprint(views.bp)

    migrate.init_app(app, db)

    return app
