"""init pr_skill

Revision ID: bfd48b6dca21
Revises: 62c172329a35
Create Date: 2022-04-20 13:21:06.390526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfd48b6dca21'
down_revision = '62c172329a35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'pr_skill',
        sa.Column('pr_id', sa.Integer(), nullable=False),
        sa.Column('skill_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['pr_id'], ['pull_request.id'], name=op.f('fk_pr_skill_pr_id_pull_request')),
        sa.ForeignKeyConstraint(['skill_id'], ['skill.id'], name=op.f('fk_pr_skill_skill_id_skill')),
        sa.PrimaryKeyConstraint('pr_id', 'skill_id', name=op.f('pk_pr_skill')),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pr_skill')
    # ### end Alembic commands ###
