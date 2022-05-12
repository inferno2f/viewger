import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate

from app.commands import pull_gitlab_data
from app.db import db
from app.gitlab_client import gitlab_client
from app.modules import forge, main

basedir = Path(__file__).resolve().parent.parent
load_dotenv(basedir.joinpath(".env"))

migrate = Migrate()


def create_app(config: dict = None):
    app = Flask(__name__)

    app.config.from_object(os.environ["APP_SETTINGS"])

    if config:
        app.config.update(config)

    logging.basicConfig(level=app.config['LOG_LEVEL'], format='%(asctime)s %(levelname)s %(name)s %(message)s')

    db.init_app(app)
    gitlab_client.init_app(app)
    migrate.init_app(app, db)

    # app.register_blueprint(commands.pull_gitlab_data)
    app.register_blueprint(main.views.blueprint)
    app.register_blueprint(forge.views.blueprint)

    app.cli.add_command(pull_gitlab_data)

    return app
