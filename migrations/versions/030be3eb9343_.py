"""empty message

Revision ID: 030be3eb9343
Revises: 18f544dbdad2
Create Date: 2018-09-18 11:30:49.777808

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '030be3eb9343'
down_revision = '18f544dbdad2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('author_uuid', sa.String(length=64), nullable=True))
    op.drop_constraint('article_ibfk_1', 'article', type_='foreignkey')
    op.create_foreign_key(None, 'article', 'user', ['author_uuid'], ['user_uuid'])
    op.drop_column('article', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('author', mysql.VARCHAR(length=64), nullable=True))
    op.drop_constraint(None, 'article', type_='foreignkey')
    op.create_foreign_key('article_ibfk_1', 'article', 'user', ['author'], ['user_uuid'])
    op.drop_column('article', 'author_uuid')
    # ### end Alembic commands ###
