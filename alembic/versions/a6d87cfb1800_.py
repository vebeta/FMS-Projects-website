"""empty message

Revision ID: a6d87cfb1800
Revises: f2a171e13eb6
Create Date: 2024-04-19 21:09:25.557066

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a6d87cfb1800'
down_revision: Union[str, None] = 'f2a171e13eb6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
