"""empty message

Revision ID: 59ba75662025
Revises: ab520e184e55
Create Date: 2024-04-19 16:41:44.981218

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59ba75662025'
down_revision: Union[str, None] = 'ab520e184e55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
