import pytest
from app import create_app
from flask import current_app

@pytest.fixture()
def app():
    app = create_app()
    return app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_prcoess_new_mr(client):
    # Тест не рабочий, разобраться с тем достать переменную окружения
    # Тест не должен отправлять запрос к апи на присвоение ревьюера
    reviewer = current_app.config['REVIEWER_ID']
    response = client.post('/new_mr', headers={'X-Gitlab-Event': 'Merge Reqest Hook'},
                        json={'id': 14, 'project_id': 131110, 'reviewer_ids': [reviewer]})
    # test fails since webhook doesn't return any response
    # however the reviewer is assigned
    assert response.status_code == 201
        