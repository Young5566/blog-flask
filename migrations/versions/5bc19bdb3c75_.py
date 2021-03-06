"""empty message

Revision ID: 5bc19bdb3c75
Revises: 030be3eb9343
Create Date: 2018-09-18 17:29:08.487011

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5bc19bdb3c75'
down_revision = '030be3eb9343'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('tags', sa.String(length=64), nullable=False))
    op.drop_column('article', 'tages')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('tages', mysql.VARCHAR(length=64), nullable=False))
    op.drop_column('article', 'tags')
    # ### end Alembic commands ###
