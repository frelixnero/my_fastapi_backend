"""add foreign-key to posts table

Revision ID: a35a26338dce
Revises: 0eab08b9c39c
Create Date: 2024-12-26 15:33:18.947162

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a35a26338dce'
down_revision: Union[str, None] = '0eab08b9c39c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable = False))
    op.create_foreign_key("posts_users_fk", source_table = "posts", referent_table = "users",
                          local_cols = ["owner_id"], remote_cols = ["id"], ondelete = "CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name = "posts")
    op.drop_column("posts", "owner_id")
    pass
