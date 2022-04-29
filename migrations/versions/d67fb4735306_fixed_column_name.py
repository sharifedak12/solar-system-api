"""fixed column name

Revision ID: d67fb4735306
Revises: 9557fc207db6
Create Date: 2022-04-29 15:49:55.683954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd67fb4735306'
down_revision = '9557fc207db6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet', sa.Column('description', sa.String(), nullable=False))
    op.drop_column('planet', 'desciption')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet', sa.Column('desciption', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('planet', 'description')
    # ### end Alembic commands ###