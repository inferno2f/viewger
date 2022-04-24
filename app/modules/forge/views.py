import logging
import gitlab
import requests
from flask import current_app, Blueprint, request

from app.modules.forge.review_manager import ReviewManager

blueprint = Blueprint("forge", __name__)


@blueprint.route('/new_mr', methods=['POST'])
def process_new_mr():
    if request.headers['X-Gitlab-Event'] == 'Merge Request Hook':
        project_id = request.json['project_id']
        mr_id = request.json['id']
        client = gitlab.Gitlab(current_app.config['GITLAB_URL'], private_token=current_app.config['GITLAB_TOKEN'])
        manager = ReviewManager(client)
        try:
            manager.assign_reviewer(project_id, mr_id)
            return requests.Response(status=201)
        except Exception as e:
            return logging.info(f'API response: {e}')
