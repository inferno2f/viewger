from app.db import db


class PullRequest(db.Model):
    __tablename__ = "pull_request"

    id = db.Column(db.Integer, primary_key=True)
    jira_task_id = db.Column(db.Integer, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    opened_at = db.Column(db.DateTime, nullable=False)
    closed_at = db.Column(db.DateTime, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)

    reviews = db.relationship('Review', backref=db.backref('pull_request', lazy=True))

    def __repr__(self):
        return f"{self.jira_task_id} - id: {self.id}"


class Review(db.Model):
    __tablename__ = "review"

    id = db.Column(db.Integer, primary_key=True)
    pr_id = db.Column(db.Integer, db.ForeignKey('pull_request.id'), nullable=False)
    reviewer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    start_at = db.Column(db.DateTime, nullable=False)
    upd_at = db.Column(db.DateTime)
    status = db.Column(db.Enum(name='statuses'))

    def __repr__(self):
        return f"{self.pr_id} - id: {self.id}"
