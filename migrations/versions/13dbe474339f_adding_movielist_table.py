"""Adding movielist table

Revision ID: 13dbe474339f
Revises: b234e3902d49
Create Date: 2022-11-05 23:09:48.093564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13dbe474339f'
down_revision = 'b234e3902d49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie_list',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('overview', sa.String(length=255), nullable=True),
    sa.Column('poster', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'movie_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_list')
    # ### end Alembic commands ###
