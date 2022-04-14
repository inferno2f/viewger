import os

from pathlib import Path

from flask_migrate import Migrate
from flask import Flask
from dotenv import load_dotenv

basedir = Path(__file__).resolve().parent.parent
load_dotenv(basedir.joinpath(".env"))

migrate = Migrate()


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(os.environ["APP_SETTINGS"])

    from .db import db

    db.init_app(app)

    from .blueprints.main import main as main_blueprint

    app.register_blueprint(main_blueprint, url_prefix="/")

    from .blueprints.api import api as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api/")

    from .blueprints.admin import admin as admin_blueprint

    app.register_blueprint(admin_blueprint, url_prefix="/admin/")

    migrate.init_app(app, db)

    return app
