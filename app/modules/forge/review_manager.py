import os
import gitlab
from flask import current_app


class ReviewManager:
    # FIXME: переменные окружения не подгружаются, изучить application context в доках
    client = gitlab.Gitlab(current_app.config['GITLAB_URL'], private_token=current_app.config['GITLAB_TOKEN'])

    def assign_reviewer(self, project_id, merge_request_id, reviewer_id):
        """ Assigns a reviewer to a merge request. """
        project = self.client.projects.get(project_id)
        mr = project.mergerequests.get(merge_request_id)
        mr.manager.update(mr.get_id(), {'reviewer_ids': [reviewer_id]})
