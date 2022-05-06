import logging
import os

from app.gitlab_client import gitlab_client
from app.modules.project.models import Project

logger = logging.getLogger(__name__)


class PullProject:
    @staticmethod
    def pull_project(project_name):
        """Gets project data from site"""
        logger.info(f'Searching for {project_name} project on git.epam.com')
        project = gitlab_client.projects.get('epm-lstr/epm-lstr-vwg/' + project_name)
        os.environ["PROJECT_ID"] = str(project.id)
        return Project(id=project.id, name=project.name, description=project.description, started_at=project.created_at)
