from flask import current_app


# FIXME: переделать тест так, чтобы не шли запросы к API
def test_prcoess_new_mr(app, client):
    with app.app_context():
        reviewer = current_app.config['REVIEWER_ID']
        response = client.post(
            '/new_mr',
            headers={'X-Gitlab-Event': 'Merge Request Hook'},
            json={'id': 14, 'project_id': 131110, 'reviewer_ids': [reviewer]},
        )
        assert response.status_code == 201
