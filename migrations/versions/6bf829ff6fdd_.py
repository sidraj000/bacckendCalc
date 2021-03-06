"""empty message

Revision ID: 6bf829ff6fdd
Revises: 4ef9d97d777f
Create Date: 2020-10-07 14:00:18.618355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bf829ff6fdd'
down_revision = '4ef9d97d777f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('savings_data', sa.Column('isPrimary', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('savings_data', 'isPrimary')
    # ### end Alembic commands ###
