"""empty message

Revision ID: 30e9d3d8fccd
Revises: 5bc19bdb3c75
Create Date: 2018-09-29 15:32:53.109260

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30e9d3d8fccd'
down_revision = '5bc19bdb3c75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('abstract', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('article', 'abstract')
    # ### end Alembic commands ###
