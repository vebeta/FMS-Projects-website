"""empty message

Revision ID: f1352293e72d
Revises: 06333d5243d8
Create Date: 2024-04-19 19:58:05.462222

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1352293e72d'
down_revision: Union[str, None] = '06333d5243d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
