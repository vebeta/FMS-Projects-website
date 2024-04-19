"""empty message

Revision ID: 06333d5243d8
Revises: 6699d736aed1
Create Date: 2024-04-19 19:55:20.270247

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06333d5243d8'
down_revision: Union[str, None] = '6699d736aed1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
