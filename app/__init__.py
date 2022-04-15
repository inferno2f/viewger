import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

from app.blueprints import admin, api, main

basedir = Path(__file__).resolve().parent.parent
load_dotenv(basedir.joinpath(".env"))

migrate = Migrate()


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(os.environ["APP_SETTINGS"])

    from .db import db

    db.init_app(app)

    app.register_blueprint(admin.views.blueprint, url_prefix="/admin/")
    app.register_blueprint(api.views.blueprint, url_prefix="/api/")
    app.register_blueprint(main.views.blueprint, url_prefix="/")

    migrate.init_app(app, db)

    return app
