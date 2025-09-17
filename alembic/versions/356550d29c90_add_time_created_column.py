"""add time_created column

Revision ID: 356550d29c90
Revises: 40a7eaf9b25a
Create Date: 2024-12-27 18:33:47.466816

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '356550d29c90'
down_revision: Union[str, None] = '40a7eaf9b25a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("time_created", sa.TIMESTAMP(timezone=True), server_default = sa.text("now()"), nullable = False))
    op.add_column("users", sa.Column("time_created", sa.TIMESTAMP(timezone=True), server_default = sa.text("now()"), nullable = False))
    pass


def downgrade() -> None:
    pass
