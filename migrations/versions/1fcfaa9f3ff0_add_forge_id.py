"""add project&users forge_id

Revision ID: 1fcfaa9f3ff0
Revises: 25aa8a2fedb9
Create Date: 2022-05-16 22:56:18.267937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fcfaa9f3ff0'
down_revision = '25aa8a2fedb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('forge_id', sa.Integer(), nullable=False))
    op.create_unique_constraint(op.f('uq_project_forge_id'), 'project', ['forge_id'])
    op.add_column('users', sa.Column('forge_id', sa.Integer(), nullable=False))
    op.create_unique_constraint(op.f('uq_users_forge_id'), 'users', ['forge_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq_users_forge_id'), 'users', type_='unique')
    op.drop_column('users', 'forge_id')
    op.drop_constraint(op.f('uq_project_forge_id'), 'project', type_='unique')
    op.drop_column('project', 'forge_id')
    # ### end Alembic commands ###
