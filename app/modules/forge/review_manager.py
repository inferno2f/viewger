from app.gitlab_client import gitlab_client
from flask import current_app


class ReviewManager:
    def assign_reviewer(self, project_id, merge_request_id, reviewer_id):
        """Assigns a reviewer to a merge request."""
        try:
            project = gitlab_client.projects.get(project_id)
            mr = project.mergerequests.get(merge_request_id)
            mr.manager.update(mr.get_id(), {'reviewer_ids': [reviewer_id]})

            # TODO: предусмотреть обработку ошибок в случае кривых входных данных
        except Exception as e:
            # TODO: обращение к логгеру, когда он будет сделан
            if str(e) == '401 Unauthorized':
                return None
            else:
                return None

    def select_reviewer_for_mr(self):
        """Placeholder method for reviewer selection algorithm."""
        return current_app.config["REVIEWER_ID"]
