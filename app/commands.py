import click

from flask import current_app
from flask.cli import with_appcontext


@click.command(name='pull-gitlab-data')
@with_appcontext
def pull_gitlab_data():
    ...


current_app.cli.add_command(pull_gitlab_data)
