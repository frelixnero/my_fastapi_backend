"""add user_id column

Revision ID: 061d598a137d
Revises: 614b49ba2f29
Create Date: 2024-12-27 18:52:19.691376

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '061d598a137d'
down_revision: Union[str, None] = '614b49ba2f29'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("user_id", sa.Integer(), nullable = False))
    op.create_foreign_key("posts_users_fk", source_table = "posts", referent_table = "users",
                          local_cols = ["user_id"], remote_cols = ["id"], ondelete = "CASCADE")
    op.drop_column("posts", "created at")
    op.drop_column("users", "created at")
    
    pass


def downgrade() -> None:
    op.drop_column("posts", "users")

    pass
