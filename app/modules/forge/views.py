from flask import Blueprint, request

from app.modules.forge.review_manager import ReviewManager

blueprint = Blueprint("forge", __name__)


@blueprint.route('/new_mr', methods=['POST'])
def process_new_mr():
    if request.headers.get('X-Gitlab-Event') == 'Merge Request Hook':
        project_id = request.json.get('project_id')
        mr_id = request.json.get('id')
        manager = ReviewManager()
        reviewer_id = manager.select_reviewer_for_mr()
        manager.assign_reviewer(project_id, mr_id, reviewer_id)
        return {'status': 'created'}, 201
