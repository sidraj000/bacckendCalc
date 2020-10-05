"""empty message

Revision ID: 4ef9d97d777f
Revises: 3149b783635c
Create Date: 2020-10-05 10:56:16.891831

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ef9d97d777f'
down_revision = '3149b783635c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('savings_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userName', sa.String(), nullable=True),
    sa.Column('savings', sa.Integer(), nullable=True),
    sa.Column('salary', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('savings_data')
    # ### end Alembic commands ###
