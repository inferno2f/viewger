"""init projects

Revision ID: e92ae6e702a3
Revises: 4981b3747a43
Create Date: 2022-04-18 22:34:27.464612

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e92ae6e702a3'
down_revision = '4981b3747a43'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('description', sa.VARCHAR(), nullable=False),
    sa.Column('started_at', sa.TIMESTAMP(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_project'))
    )
    op.drop_table('review')
    op.add_column('pull_request', sa.Column('project_id', sa.Integer(), nullable=False))
    op.create_foreign_key(op.f('fk_pull_request_project_id_project'), 'pull_request', 'project', ['project_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_pull_request_project_id_project'), 'pull_request', type_='foreignkey')
    op.drop_column('pull_request', 'project_id')
    op.create_table('review',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('pr_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('reviewer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('start_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('upd_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('status', postgresql.ENUM(name='review_status'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['pr_id'], ['pull_request.id'], name='fk_review_pr_id_pull_request'),
    sa.ForeignKeyConstraint(['reviewer_id'], ['users.id'], name='fk_review_reviewer_id_users'),
    sa.PrimaryKeyConstraint('id', name='pk_review')
    )
    op.drop_table('project')
    # ### end Alembic commands ###
