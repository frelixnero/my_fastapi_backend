"""add user_id column

Revision ID: 614b49ba2f29
Revises: 356550d29c90
Create Date: 2024-12-27 18:45:32.736172

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '614b49ba2f29'
down_revision: Union[str, None] = '356550d29c90'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("posts", "owner_id")
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name = "posts")
    op.drop_column("posts", "owner_id")
    pass
