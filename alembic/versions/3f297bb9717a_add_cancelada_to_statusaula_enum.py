"""Add cancelada to StatusAula enum

Revision ID: 3f297bb9717a
Revises: ea9aa9b1eddd
Create Date: 2025-11-19 14:55:44.760300

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f297bb9717a'
down_revision: Union[str, None] = 'ea9aa9b1eddd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # MySQL não altera ENUM automaticamente, então fazemos ALTER TABLE manual
    op.execute("""
        ALTER TABLE agendas 
        MODIFY COLUMN status ENUM(
            'disponivel', 
            'em_andamento', 
            'finalizada', 
            'cancelada'
        ) 
        DEFAULT 'disponivel';
    """)

def downgrade():
    # Downgrade remove 'cancelada' (apenas se não houver linhas com esse valor)
    op.execute("""
        ALTER TABLE agendas 
        MODIFY COLUMN status ENUM(
            'disponivel', 
            'em_andamento', 
            'finalizada'
        ) 
        DEFAULT 'disponivel';
    """)

