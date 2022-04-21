from flask import Blueprint, request
from dataclasses import dataclass
from datetime import datetime

from app.modules.connector.review_manager import ReviewManager

blueprint = Blueprint("webhook", __name__)


manager = ReviewManager()

@blueprint.route('/webhook', methods=['POST'])
def webhook():
    if request.headers['X-Gitlab-Event'] == 'Merge Request Hook':
        project_id = request.json['project_id']
        mr_id = request.json['id'] 
        return manager.assign_reviewer(project_id, mr_id)
        

# @dataclass
# class GitlabMergeRequest:
#     id: int
#     merge_request_id: int
#     target_branch: str
#     source_branch: str
#     assignee_id: int
#     author_id: int
#     title: str
#     created_at: datetime
#     updated_at: datetime
#     description: str

# def old_webhook_code():
#     if request.headers['X-Gitlab-Event'] == 'Merge Request Hook':
#         payload = request.json
#         mr = GitlabMergeRequest(
#             id=payload['labels'][0]['id'],
#             merge_request_id=payload['object_attributes']['id'],
#             target_branch=payload['object_attributes']['target_branch'],
#             source_branch=payload['object_attributes']['source_branch'],
#             assignee_id=payload['object_attributes']['assignee_id'],
#             author_id=payload['object_attributes']['author_id'],
#             title=payload['object_attributes']['title'],
#             created_at=payload['object_attributes']['created_at'],
#             updated_at=payload['object_attributes']['updated_at'],
#             description=payload['object_attributes']['description'],
#         )
#         return {'result': mr.__dict__}
