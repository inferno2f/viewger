from app.gitlab_client import gitlab_client
from flask import current_app


class ReviewManager:
    def assign_reviewer(self, project_id, merge_request_id, reviewer_id):
        """Assigns a reviewer to a merge request."""
        project = gitlab_client.projects.get(project_id)
        mr = project.mergerequests.get(merge_request_id)
        mr.manager.update(mr.get_id(), {'reviewer_ids': [reviewer_id]})

    def select_reviewer_for_mr(self):
        """Placeholder method for reviewer selection algorithm."""
        return current_app.config['REVIEWER_ID']
