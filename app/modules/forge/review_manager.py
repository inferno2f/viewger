from flask import current_app

from app.gitlab_client import gitlab_client
from app.logger_config import logger

logger.name = __name__


class ReviewManager:
    def assign_reviewer(self, project_id, merge_request_id, reviewer_id):
        """Assigns a reviewer to a merge request."""
        project = gitlab_client.projects.get(project_id)
        mr = project.mergerequests.get(merge_request_id)
        logger.info(f'Assigning reviewer {reviewer_id} to merge request {mr.iid}')
        mr.manager.update(mr.get_id(), {'reviewer_ids': [reviewer_id]})

    def select_reviewer_for_mr(self):
        """Placeholder method for reviewer selection algorithm."""
        logger.info('Selecting reviewer for merge request')
        return current_app.config['REVIEWER_ID']
