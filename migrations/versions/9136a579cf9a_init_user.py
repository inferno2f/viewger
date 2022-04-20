"""init user

Revision ID: 9136a579cf9a
Revises: 8d296729bd1f
Create Date: 2022-04-20 13:11:12.654205

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9136a579cf9a'
down_revision = '8d296729bd1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'result_no_stop_words')
    op.drop_column('users', 'result_all')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('result_all', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('result_no_stop_words', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
