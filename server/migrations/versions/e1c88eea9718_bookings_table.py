"""bookings table

Revision ID: e1c88eea9718
Revises: 53eeb022e786
Create Date: 2024-04-15 18:28:19.259962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1c88eea9718'
down_revision = '53eeb022e786'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bookings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('stylist', sa.String(), nullable=True))
        batch_op.drop_column('customer')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bookings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('customer', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('stylist')

    # ### end Alembic commands ###
