import logging

import requests
from flask import Blueprint, request

from app.modules.forge.review_manager import ReviewManager

blueprint = Blueprint("forge", __name__)


manager = ReviewManager()


@blueprint.route('/new_mr', methods=['POST'])
def process_new_mr():
    try:
        if request.headers['X-Gitlab-Event'] == 'Merge Request Hook':
            project_id = request.json['project_id']
            mr_id = request.json['id']
            manager.assign_reviewer(project_id, mr_id)
            return requests.Response(status=201)
    except Exception as e:
        return logging.info(f'API response: {e}')
