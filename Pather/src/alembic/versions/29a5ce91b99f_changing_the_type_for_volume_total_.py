"""changing the type for: volume, total, count_

Revision ID: 29a5ce91b99f
Revises: d859557f77bb
Create Date: 2025-01-20 19:08:51.797761

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '29a5ce91b99f'
down_revision: Union[str, None] = 'd859557f77bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('spimex_trading_results', 'volume',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.Integer(),
               postgresql_using="volume::integer",
               existing_nullable=False)
    op.alter_column('spimex_trading_results', 'total',
               existing_type=sa.VARCHAR(length=128),
               postgresql_using="volume::integer",
               type_=sa.Integer(),
               existing_nullable=False)
    op.alter_column('spimex_trading_results', 'count',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.Integer(),
               postgresql_using="volume::integer",
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('spimex_trading_results', 'count',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)
    op.alter_column('spimex_trading_results', 'total',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)
    op.alter_column('spimex_trading_results', 'volume',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)
    # ### end Alembic commands ###
