"""empty message

Revision ID: 8d296729bd1f
Revises:
Create Date: 2022-04-11 16:46:17.486452

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "8d296729bd1f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=64), nullable=False),
        sa.Column("email", sa.String(length=128), unique=True, nullable=True),
        sa.Column("grade", sa.String(length=24), nullable=True),
        sa.Column(
            "is_admin", sa.Boolean(), server_default=sa.text("false"), nullable=False
        ),
        sa.Column("result_all", postgresql.JSON(astext_type=sa.Text()), nullable=True),
        sa.Column(
            "result_no_stop_words",
            postgresql.JSON(astext_type=sa.Text()),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )


def downgrade():
    op.drop_table("users")
