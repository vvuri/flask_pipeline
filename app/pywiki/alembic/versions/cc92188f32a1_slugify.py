"""Slugify

Revision ID: cc92188f32a1
Revises: 995153f9b9f3
Create Date: 2021-12-06 00:56:01.190233

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc92188f32a1'
down_revision = '995153f9b9f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'post', ['slug'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='unique')
    # ### end Alembic commands ###
