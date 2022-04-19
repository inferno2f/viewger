"""init user_skill

Revision ID: 59da48cba125
Revises: 2927aee8910d
Create Date: 2022-04-18 23:29:05.298450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59da48cba125'
down_revision = '2927aee8910d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_skill',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('skill_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['skill_id'], ['skill.id'], name=op.f('fk_user_skill_skill_id_skill')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_user_skill_user_id_users')),
    sa.PrimaryKeyConstraint('user_id', name=op.f('pk_user_skill'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_skill')
    # ### end Alembic commands ###
