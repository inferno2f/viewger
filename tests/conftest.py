import pytest
from app import create_app


@pytest.fixture()
def app():
    app = create_app()
    return app


@pytest.fixture
def create_configured_app():
    def _create_app(config: dict):
        return create_app(config)
    return _create_app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
