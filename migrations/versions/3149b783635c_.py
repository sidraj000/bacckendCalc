"""empty message

Revision ID: 3149b783635c
Revises: 97ad7980dcf0
Create Date: 2020-10-01 18:28:22.586980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3149b783635c'
down_revision = '97ad7980dcf0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('savings_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userName', sa.String(), nullable=True),
    sa.Column('savings', sa.Integer(), nullable=True),
    sa.Column('salary', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('savingsData')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('savingsData',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"savingsData_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('salary', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('savings', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('userName', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='savingsData_pkey')
    )
    op.drop_table('savings_data')
    # ### end Alembic commands ###
