"""add users table

Revision ID: 0eab08b9c39c
Revises: 0b7c7dfec7a9
Create Date: 2024-12-26 15:20:01.546115

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0eab08b9c39c'
down_revision: Union[str, None] = '0b7c7dfec7a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users", sa.Column("id", sa.Integer(), nullable = False),
                    sa.Column("email", sa.String(), nullable = False),
                    sa.Column("password", sa.String(), nullable = False),
                    sa.Column("created at", sa.TIMESTAMP(timezone=True), server_default = sa.text("now()"), nullable = False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
