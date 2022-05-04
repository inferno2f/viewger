import click
import logging

# from flask import Blueprint
from flask.cli import with_appcontext

# pull_gitlab_data = Blueprint('pull_gitlab_data', __name__)

logger = logging.getLogger(__name__)


@click.command(name='pull_gitlab_data')
@with_appcontext
def pull_gitlab_data():
    """Pulling project's data from Gitlab"""
    logger.info("Pulling project's data from Gitlab")
    print("Pulling project's data from Gitlab")
