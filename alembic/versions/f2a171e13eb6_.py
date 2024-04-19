"""empty message

Revision ID: f2a171e13eb6
Revises: b4a8fc1c4b18
Create Date: 2024-04-19 21:08:02.684012

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f2a171e13eb6'
down_revision: Union[str, None] = 'b4a8fc1c4b18'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
