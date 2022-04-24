import pytest
from app import create_app
from flask import current_app


@pytest.fixture()
def app():
    app = create_app()
    return app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():
            assert current_app.config["ENV"] == "production"
        yield client


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
