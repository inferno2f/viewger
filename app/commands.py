import click
import logging

from app.services import pull_project_data, pull_project_members
from flask import current_app
from flask.cli import with_appcontext

logger = logging.getLogger()


@click.command(name='pull_gitlab_data')
@with_appcontext
def pull_gitlab_data():
    """Pulling project's data from Gitlab"""
    logger.info("Pulling project's data from Gitlab")

    project_name = current_app.config['OBSERVED_PROJECT_NAME']
    observed_project = pull_project_data(project_name)
    pull_project_members(observed_project)
