"""empty message

Revision ID: 97ad7980dcf0
Revises: de630ed50430
Create Date: 2020-10-01 18:02:07.961072

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97ad7980dcf0'
down_revision = 'de630ed50430'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('savingsData', sa.Column('userName', sa.String(), nullable=True))
    op.drop_column('savingsData', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('savingsData', sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('savingsData', 'userName')
    # ### end Alembic commands ###
