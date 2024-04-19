"""empty message

Revision ID: 215f200703a5
Revises: 59ba75662025
Create Date: 2024-04-19 16:42:47.131800

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '215f200703a5'
down_revision: Union[str, None] = '59ba75662025'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
