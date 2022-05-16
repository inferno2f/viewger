import logging
import os

from app.db import db
from app.gitlab_client import gitlab_client as gl
from app.modules.project.models import Project
from app.modules.user.models import User

logger = logging.getLogger(__name__)


class ViewgerServices:
    @staticmethod
    def pull_project_data(project_name: str) -> Project:
        """
        Gets project data from site
        """
        logger.info(f'Searching for {project_name} project on git.epam.com')
        project_name_space = f'epm-lstr/epm-lstr-vwg/{project_name}'
        project = gl.projects.get(project_name_space)
        os.environ['PROJECT_ID'] = str(project.id)
        project_data = Project(
            id=project.id, name=project.name, description=project.description, started_at=project.created_at
        )
        if not Project.query.filter_by(id=project.id).first():
            db.session.add(project_data)
            db.session.commit()
        return project_data

    @staticmethod
    def pull_project_members(project: Project) -> None:
        """
        Fetch members of a project from GitLab API, add them to the database
        :param project: Project
        """
        logger.info(f'Fetching members of {project.name} project')
        project = gl.projects.get(project.id)
        members = project.members.list()
        for member in members:
            if not User.query.filter_by(username=member.attributes.get('username')).first():
                user = User(id=member.id, username=member.username)
                db.session.add(user)
                db.session.commit()
