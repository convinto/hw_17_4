"""empty message

Revision ID: 29f0ad739a8b
Revises: 4dd0710e255b
Create Date: 2024-12-16 22:54:46.933785

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '29f0ad739a8b'
down_revision: Union[str, None] = '4dd0710e255b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
