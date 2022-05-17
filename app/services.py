import logging

from app.db import db
from app.gitlab_client import gitlab_client as gl
from app.modules.project.models import Project
from app.modules.user.models import User

logger = logging.getLogger()


class ViewgerServices:
    def __init__(self, project_name):
        self.project_name = project_name
        project_name_space = f'epm-lstr/epm-lstr-vwg/{self.project_name}'
        self.project = gl.projects.get(project_name_space)

    def pull_project_data(self) -> Project:
        """
        Gets project data from site
        """
        logger.info(f'Searching for {self.project_name} project on git.epam.com')
        project_data = Project(
            forge_id=self.project.id,
            name=self.project.name,
            description=self.project.description,
            started_at=self.project.created_at,
        )
        if not Project.query.filter_by(forge_id=self.project.id).first():
            db.session.add(project_data)
            db.session.commit()
        return project_data

    def pull_project_members(self) -> None:
        """
        Fetch members of a project from GitLab API, add them to the database
        """
        logger.info(f'Fetching members of {self.project.name} project')
        members = self.project.members.list()
        for member in members:
            if not User.query.filter_by(username=member.attributes.get('username')).first():
                user = User(forge_id=member.id, username=member.username)
                db.session.add(user)
                db.session.commit()
