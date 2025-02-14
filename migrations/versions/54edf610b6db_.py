"""empty message

Revision ID: 54edf610b6db
Revises: 
Create Date: 2025-01-14 11:59:50.969793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54edf610b6db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('is_done', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###
