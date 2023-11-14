"""entries

Revision ID: c3630ab79551
Revises: d68a85b8091b
Create Date: 2023-11-14 16:00:22.412246

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c3630ab79551'
down_revision = 'd68a85b8091b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'entries',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('value', sa.Integer(), nullable=True),
        sa.Column('datetime', sa.TIMESTAMP, nullable=True),
        sa.Column('note', sa.String(500), nullable=True),
        sa.Column('tag', sa.String(25), nullable=True),
        sa.Column('item_id', sa.Integer(), nullable=True),
        sa.Column('updated_date', sa.TIMESTAMP, nullable=True),
        sa.Column('deleted_date', sa.TIMESTAMP, server_default=sa.func.now(), nullable=True),
        sa.Column('updated_by', sa.String(100), nullable=True),
        sa.Column('deleted_by', sa.String(100), nullable=True),

    )


def downgrade():
    pass
