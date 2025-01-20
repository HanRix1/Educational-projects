"""Add Spimex_trading_results table

Revision ID: d859557f77bb
Revises: 
Create Date: 2025-01-20 03:47:31.181007

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd859557f77bb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('spimex_trading_results',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('exchange_product_id', sa.String(length=128), nullable=False),
    sa.Column('exchange_product_name', sa.String(length=128), nullable=False),
    sa.Column('oil_id', sa.String(length=128), nullable=False),
    sa.Column('delivery_basis_id', sa.String(length=128), nullable=False),
    sa.Column('delivery_basis_name', sa.String(length=128), nullable=False),
    sa.Column('delivery_type_id', sa.String(length=128), nullable=False),
    sa.Column('volume', sa.String(length=128), nullable=False),
    sa.Column('total', sa.String(length=128), nullable=False),
    sa.Column('count', sa.String(length=128), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_spimex_trading_results'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('spimex_trading_results')
    # ### end Alembic commands ###
