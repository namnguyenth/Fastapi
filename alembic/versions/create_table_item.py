"""item

Revision ID: d68a85b8091b
Revises: 0806fbdd513c
Create Date: 2023-11-06 15:23:30.599520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd68a85b8091b'
down_revision = '0806fbdd513c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'item',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(200), nullable=True),
        sa.Column('category_id', sa.Integer(), nullable=True),
        sa.Column('updated_date', sa.TIMESTAMP, server_default=sa.func.now(), nullable=True),
        sa.Column('deleted_date', sa.TIMESTAMP, server_default=sa.func.now(), nullable=True),
        sa.Column('updated_by', sa.String(100), nullable=True),
        sa.Column('deleted_by', sa.String(100), nullable=True)

    )


def downgrade():
    pass
