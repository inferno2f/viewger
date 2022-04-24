class ReviewManager:
    def __init__(self, client):
        self.client = client

    def assign_reviewer(self, project_id, merge_request_id, reviewer_id):
        """Assigns a reviewer to a merge request."""
        project = self.client.projects.get(project_id)
        mr = project.mergerequests.get(merge_request_id)
        mr.manager.update(mr.get_id(), {'reviewer_ids': [reviewer_id]})
