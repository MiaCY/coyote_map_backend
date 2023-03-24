"""empty message

Revision ID: 0f86706696fc
Revises: 
Create Date: 2023-03-23 16:19:11.039495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f86706696fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coyote_map_images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('imageName', sa.String(), nullable=False),
    sa.Column('imageUrl', sa.String(), nullable=False),
    sa.Column('imageRegion', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('coyote_map_images')
    # ### end Alembic commands ###
