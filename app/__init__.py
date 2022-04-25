import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

from app.db import db
from app.gitlab_client import gitlab_client
from app.modules import forge, main

basedir = Path(__file__).resolve().parent.parent
load_dotenv(basedir.joinpath(".env"))

migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object(os.environ["APP_SETTINGS"])

    db.init_app(app)
    gitlab_client.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main.views.blueprint)
    app.register_blueprint(forge.views.blueprint)

    return app
