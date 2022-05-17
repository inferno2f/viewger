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
        logger.info(f'Searching for {self.project_name} project on git.epam.com')
        self.project = gl.projects.get(project_name_space)

    def pull_project_data(self) -> Project:
        """
        Fetch project info from gitlab.project & add them to the db
        """
        project_data = Project(
            forge_id=self.project.id,
            name=self.project.name,
            description=self.project.description,
            started_at=self.project.created_at,
        )
        if not Project.query.first():
            db.session.add(project_data)
            logger.info(f'Fetching {self.project_name} project info')
            db.session.commit()
        else:
            Project.query.update(
                {
                    'forge_id': self.project.id,
                    'name': self.project.name,
                    'description': self.project.description,
                    'started_at': self.project.created_at,
                }
            )
            logger.info(f'Updating {self.project_name} project info')
            db.session.commit()
        return project_data

    def pull_project_members(self) -> None:
        """
        Fetch members of a project from gitlab.project & add them to the db
        """
        logger.info(f'Fetching members of {self.project.name} project')
        members = self.project.members.list()
        for member in members:
            if not User.query.filter_by(username=member.attributes.get('username')).first():
                user = User(forge_id=member.id, username=member.username)
                db.session.add(user)
                db.session.commit()
