"""Add fields for questionnaire responses

Revision ID: b129eb634232
Revises: 5f40c8bda3bd
Create Date: 2025-01-14 15:12:31.731356

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b129eb634232'
down_revision = '5f40c8bda3bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('p1', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('p2', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('p3', sa.String(length=50), nullable=False))
        batch_op.drop_column('idade')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('idade', sa.INTEGER(), nullable=False))
        batch_op.drop_column('p3')
        batch_op.drop_column('p2')
        batch_op.drop_column('p1')
        batch_op.drop_column('email')

    # ### end Alembic commands ###
