import pytest

from app import create_app


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


def test_webhook(client):
    response = client.post('/webhook', headers={'X-Gitlab-Event': 'Merge Request Hook'},
                           json={'id': 14, 'project_id': 131110})
    # test fails since webhook doesn't return any response
    # however the reviewer is assigned
    assert response.status_code == 200
    