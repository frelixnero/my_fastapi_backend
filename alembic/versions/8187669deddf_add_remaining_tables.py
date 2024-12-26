"""add remaining Columns

Revision ID: 8187669deddf
Revises: a35a26338dce
Create Date: 2024-12-26 16:00:24.558933

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8187669deddf'
down_revision: Union[str, None] = 'a35a26338dce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable = False, server_default = "True"))
    op.add_column("posts", sa.Column("created at", sa.TIMESTAMP(timezone=True), server_default = sa.text("now()"), nullable = False))
                  
    
    pass


def downgrade() -> None:
    op.drop_column("posts", "published")
    op.drop_column("posts", "created at")
    pass
