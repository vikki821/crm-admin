"""empty message

Revision ID: 3b50db5d99a7
Revises: 7b8c4d0267c4
Create Date: 2020-03-09 19:05:14.731851

"""

# revision identifiers, used by Alembic.
revision = '3b50db5d99a7'
down_revision = '7b8c4d0267c4'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('phone', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('gym_account')
    op.add_column('member', sa.Column('account_id', sa.Integer(), nullable=True))
    op.drop_column('member', 'gym_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('member', sa.Column('gym_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('member', 'account_id')
    op.create_table('gym_account',
    sa.Column('id', mysql.INTEGER(), nullable=False),
    sa.Column('email', mysql.VARCHAR(collation='utf8mb4_general_ci', length=255), nullable=True),
    sa.Column('password', mysql.VARCHAR(collation='utf8mb4_general_ci', length=255), nullable=True),
    sa.Column('name', mysql.VARCHAR(collation='utf8mb4_general_ci', length=255), nullable=True),
    sa.Column('phone', mysql.VARCHAR(collation='utf8mb4_general_ci', length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_general_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('account')
    ### end Alembic commands ###
