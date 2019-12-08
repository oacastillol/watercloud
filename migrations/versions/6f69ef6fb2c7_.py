"""empty message

Revision ID: 6f69ef6fb2c7
Revises: 
Create Date: 2019-12-08 02:37:29.346534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f69ef6fb2c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('samples',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('device', sa.Integer(), nullable=False),
    sa.Column('sensores', sa.JSON(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('recepted_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('samples')
    # ### end Alembic commands ###
