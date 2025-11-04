"""Alter tipo_admin to varchar

Revision ID: 07505766e5c3
Revises: aaab08ca480d
Create Date: 2025-11-04 02:49:01.221179

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '07505766e5c3'
down_revision: Union[str, None] = 'aaab08ca480d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


from alembic import op
import sqlalchemy as sa

def upgrade():
    op.alter_column('admins', 'tipo_admin',
        existing_type=sa.Enum('admin_pleno', 'recepcionista', name='tipoadmin'),
        type_=sa.String(20),
        existing_nullable=False
    )

def downgrade():
    op.alter_column('admins', 'tipo_admin',
        existing_type=sa.String(20),
        type_=sa.Enum('admin_pleno', 'recepcionista', name='tipoadmin'),
        existing_nullable=False
    )

