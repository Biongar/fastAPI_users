"""add not null setting

Revision ID: 394535c6db36
Revises: b5b61eac7789
Create Date: 2022-09-15 23:00:27.236197

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '394535c6db36'
down_revision = 'b5b61eac7789'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('account_user', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('account_user', 'is_admin',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('account_user', 'is_superuser',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('account_user', 'date_created',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('account_user', 'date_updated',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.create_unique_constraint(None, 'account_user', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'account_user', type_='unique')
    op.alter_column('account_user', 'date_updated',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('account_user', 'date_created',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('account_user', 'is_superuser',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('account_user', 'is_admin',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('account_user', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
