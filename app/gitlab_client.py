from flask import Flask
from gitlab import Gitlab


class GitlabClient:
    _client = None

    def init_app(self, app: Flask):
        self._client = Gitlab(app.config['GITLAB_URL'], private_token=app.config['GITLAB_TOKEN'])

    def __getattr__(self, item):
        return getattr(self._client, item)


gitlab_client = GitlabClient()
