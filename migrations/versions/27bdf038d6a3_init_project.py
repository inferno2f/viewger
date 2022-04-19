"""init project

Revision ID: 27bdf038d6a3
Revises: 4981b3747a43
Create Date: 2022-04-18 23:10:23.680794

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27bdf038d6a3'
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
    op.add_column('pull_request', sa.Column('project_id', sa.Integer(), nullable=False))
    op.create_foreign_key(op.f('fk_pull_request_project_id_project'), 'pull_request', 'project', ['project_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_pull_request_project_id_project'), 'pull_request', type_='foreignkey')
    op.drop_column('pull_request', 'project_id')
    op.drop_table('project')
    # ### end Alembic commands ###
