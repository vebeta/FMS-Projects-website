"""empty message

Revision ID: b4a8fc1c4b18
Revises: f1352293e72d
Create Date: 2024-04-19 20:51:47.819600

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4a8fc1c4b18'
down_revision: Union[str, None] = 'f1352293e72d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
