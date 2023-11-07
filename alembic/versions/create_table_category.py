"""category

Revision ID: 0806fbdd513c
Revises: 
Create Date: 2023-11-06 15:07:49.909361

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0806fbdd513c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'category',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('title', sa.String(200), nullable=True),
        sa.Column('priority', sa.Integer(), nullable=True),
        sa.Column('updated_date', sa.TIMESTAMP, server_default=sa.func.now(), nullable=True),
        sa.Column('deleted_date', sa.TIMESTAMP, server_default=sa.func.now(), nullable=True),
        sa.Column('updated_by', sa.String(100), nullable=True),
        sa.Column('deleted_by', sa.String(100), nullable=True)

    )


def downgrade():
    pass
