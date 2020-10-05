"""empty message

Revision ID: bd0899cb0d3e
Revises: e462535be42f
Create Date: 2020-10-01 17:55:27.602440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd0899cb0d3e'
down_revision = 'e462535be42f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('savingsData', sa.Column('doors', sa.Integer(), nullable=True))
    op.add_column('savingsData', sa.Column('model', sa.String(), nullable=True))
    op.add_column('savingsData', sa.Column('name', sa.String(), nullable=True))
    op.drop_column('savingsData', 'salary')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('savingsData', sa.Column('salary', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('savingsData', 'name')
    op.drop_column('savingsData', 'model')
    op.drop_column('savingsData', 'doors')
    # ### end Alembic commands ###