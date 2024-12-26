"""add content column to posts table

Revision ID: 0b7c7dfec7a9
Revises: 79016498df16
Create Date: 2024-12-26 14:21:39.075992

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0b7c7dfec7a9'
down_revision: Union[str, None] = '79016498df16'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable = False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
