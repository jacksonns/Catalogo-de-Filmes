"""add movies list

Revision ID: e93ab122e88a
Revises: 13dbe474339f
Create Date: 2022-11-06 12:50:13.870866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e93ab122e88a'
down_revision = '13dbe474339f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_list')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('wantToWatchList', sa.PickleType(), nullable=True))
        batch_op.add_column(sa.Column('watchedList', sa.PickleType(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('watchedList')
        batch_op.drop_column('wantToWatchList')

    op.create_table('movie_list',
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('movie_id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), nullable=True),
    sa.Column('overview', sa.VARCHAR(length=255), nullable=True),
    sa.Column('poster', sa.VARCHAR(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'movie_id')
    )
    # ### end Alembic commands ###