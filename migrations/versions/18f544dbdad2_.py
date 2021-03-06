"""empty message

Revision ID: 18f544dbdad2
Revises: 
Create Date: 2018-09-18 10:47:22.458639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18f544dbdad2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_uuid', sa.String(length=64), nullable=False),
    sa.Column('user_name', sa.String(length=64), nullable=False),
    sa.Column('password_hash', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('user_uuid')
    )
    op.create_table('article',
    sa.Column('article_uuid', sa.String(length=64), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('tages', sa.String(length=64), nullable=False),
    sa.Column('author', sa.String(length=64), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author'], ['user.user_uuid'], ),
    sa.PrimaryKeyConstraint('article_uuid')
    )
    op.create_index(op.f('ix_article_time'), 'article', ['time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_article_time'), table_name='article')
    op.drop_table('article')
    op.drop_table('user')
    # ### end Alembic commands ###
