"""empty message

Revision ID: 73c9f84268a7
Revises: e90472f3ee9f
Create Date: 2020-10-01 17:58:51.340039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73c9f84268a7'
down_revision = 'e90472f3ee9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('savingsData', sa.Column('salary', sa.Integer(), nullable=True))
    op.drop_column('savingsData', 'salar')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('savingsData', sa.Column('salar', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('savingsData', 'salary')
    # ### end Alembic commands ###