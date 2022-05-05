from app.db import db
from app.gitlab_client import gitlab_client as gl
from app.modules.project.models import Project
from app.modules.user.models import User


class ViewgerServices:
    def get_project_members(self, project: Project):
        """
        Fetch members of a project from GitLab API, add them to the database
        :param project: Project
        """
        project = gl.projects.get(project.id)
        members = project.members.list()
        for member in members:
            if not User.query.filter_by(username=member.attributes.get('username')).first():
                user = User(id=member.id, username=member.username)
                db.session.add(user)
                db.session.commit()
