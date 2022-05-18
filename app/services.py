import logging

from app.db import db
from app.gitlab_client import gitlab_client as gl
from app.modules.project.models import Project
from app.modules.user.models import User

logger = logging.getLogger()


def create_or_update_object(object_type: str, object_data: dict) -> object:
    """
    Create or update an object in the database
    :param object_type: str
    :param object_data: dict
    """
    observed_object = object_type.query.filter_by(forge_id=object_data['forge_id']).first()
    if observed_object:
        db.session.merge(object_type(**object_data))
        logger.info(f'{object_type.__name__} {object_data["forge_id"]} already exists in the database, updating data')
    else:
        db.session.add(object_type(**object_data))
        logger.info(f'Added {object_type.__name__} {object_data["forge_id"]} to the database')
    db.session.commit()
    return object_type.query.filter_by(forge_id=object_data['forge_id']).first()


def pull_project_data(project_name: str) -> Project:
    """
    Gets project data from site
    """
    logger.info(f'Searching for {project_name} project on git.epam.com')
    project_name_space = f'epm-lstr/epm-lstr-vwg/{project_name}'
    project = gl.projects.get(project_name_space)
    project_data = {
        'forge_id': project.id,
        'name': project.name,
        'description': project.description,
        'started_at': project.created_at,
    }
    project = create_or_update_object(Project, project_data)
    return project


def pull_project_members(project: Project) -> None:
    """
    Fetch members of a project from GitLab API, add them to the database
    :param project: Project
    """
    logger.info(f'Fetching members of {project.name} project')
    project = gl.projects.get(project.forge_id)
    members = project.members.list()
    for member in members:
        user_data = {
            'forge_id': member.id,
            'username': member.username,
        }
        create_or_update_object(User, user_data)
