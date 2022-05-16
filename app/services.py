import logging

from app.db import db
from app.gitlab_client import gitlab_client as gl
from app.modules.project.models import Project
from app.modules.user.models import User

logger = logging.getLogger()


class ViewgerServices:
    @staticmethod
    def pull_project_data(project_name):
        """
        Gets project data from site
        """
        logger.info(f'Searching for {project_name} project on git.epam.com')
        project = gl.projects.get('epm-lstr/epm-lstr-vwg/' + project_name)
        project_data = Project(
            forge_id=project.id, name=project.name, description=project.description, started_at=project.created_at
        )
        if not Project.query.filter_by(forge_id=project.id).first():
            db.session.add(project_data)
            db.session.commit()

        members = project.members.list()
        for member in members:
            if not User.query.filter_by(username=member.attributes.get('username')).first():
                user = User(forge_id=member.id, username=member.username)
                db.session.add(user)
                db.session.commit()
