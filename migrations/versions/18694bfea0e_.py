"""empty message

Revision ID: 18694bfea0e
Revises: 38c4e85512a9
Create Date: 2016-05-21 09:11:42.163246

"""

# revision identifiers, used by Alembic.
revision = '18694bfea0e'
down_revision = '38c4e85512a9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('users', sa.Column('password_hash', sa.String(32)))


def downgrade():
    op.drop_column('users', 'password_hash')
