"""empty message

Revision ID: de630ed50430
Revises: 73c9f84268a7
Create Date: 2020-10-01 18:00:38.205854

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de630ed50430'
down_revision = '73c9f84268a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('savingsData', sa.Column('savings', sa.Integer(), nullable=True))
    op.add_column('savingsData', sa.Column('username', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('savingsData', 'username')
    op.drop_column('savingsData', 'savings')
    # ### end Alembic commands ###
