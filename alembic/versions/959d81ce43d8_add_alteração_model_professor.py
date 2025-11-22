"""Add alteração model professor

Revision ID: 959d81ce43d8
Revises: 3f297bb9717a
Create Date: 2025-11-19 15:13:36.591179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '959d81ce43d8'
down_revision: Union[str, None] = '3f297bb9717a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
