"""add substituto_id to agendas

Revision ID: e93daec0d348
Revises: 959d81ce43d8
Create Date: 2025-11-25 20:14:05.440846

"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'e93daec0d348'
 # mantenha o que o Alembic gerar automaticamente
down_revision: Union[str, None] = '959d81ce43d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'agendas',
        sa.Column('substituto_id', sa.Integer(), nullable=True)
    )

    op.create_foreign_key(
        'fk_agendas_substituto',
        'agendas',
        'professores',
        ['substituto_id'],
        ['id']
    )


def downgrade() -> None:
    op.drop_constraint('fk_agendas_substituto', 'agendas', type_='foreignkey')
    op.drop_column('agendas', 'substituto_id')
