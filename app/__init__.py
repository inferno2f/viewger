import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

basedir = Path(__file__).resolve().parent.parent
load_dotenv(basedir.joinpath(".env"))

migrate = Migrate()


def create_app():
    # create and configure the app
    app = Flask(__name__)

    app.config.from_object(os.environ["APP_SETTINGS"])

    from app.db import db
    from app.modules import forge, main

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main.views.blueprint)
    app.register_blueprint(forge.views.blueprint)

    return app
