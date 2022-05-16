import datetime

from flask import current_app
from app.modules.forge.review_manager import ReviewManager
from app.modules.project.models import Project
from app.services import ViewgerServices


def test_process_new_mr(app, client, monkeypatch):
    def mocked_assign(*args):
        return {'status': 'created'}, 201

    monkeypatch.setattr(ReviewManager, 'assign_reviewer', mocked_assign)

    with app.app_context():
        reviewer = current_app.config['REVIEWER_ID']
        response = client.post(
            '/new_mr',
            headers={'X-Gitlab-Event': 'Merge Request Hook'},
            json={'id': 14, 'project_id': 131110, 'reviewer_ids': [reviewer]},
        )
        assert response.status_code == 201


def test_pull_project(app, client, monkeypatch):
    def mocked_pull(*args):
        return Project(forge_id=131110, name='viewger', description=None, started_at=datetime.datetime.now())

    monkeypatch.setattr(ViewgerServices, 'pull_project_data', mocked_pull)

    with app.app_context():
        p = ViewgerServices()
        project = p.pull_project_data('viewger')
        assert project.forge_id == 131110
