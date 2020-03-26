"""empty message

Revision ID: ddd07c71ffd3
Revises: 
Create Date: 2020-03-26 11:17:01.615238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ddd07c71ffd3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roomAl1',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sentence', sa.String(length=300), nullable=False),
    sa.Column('login_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['login_id'], ['login.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=255), nullable=False),
    sa.Column('lname', sa.String(length=255), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('login_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['login_id'], ['login.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('roomAl1')
    op.drop_table('login')
    # ### end Alembic commands ###