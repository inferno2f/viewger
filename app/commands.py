import click
import logging

from app.modules.forge.pull_project import PullProject
from flask import current_app
from flask.cli import with_appcontext

logger = logging.getLogger(__name__)


@click.command(name='pull_gitlab_data')
@with_appcontext
def pull_gitlab_data():
    """Pulling project's data from Gitlab"""
    logger.info("Pulling project's data from Gitlab")
    p = PullProject()
    p.pull_project(current_app.config['OBSERVED_PROJECT_NAME'])
