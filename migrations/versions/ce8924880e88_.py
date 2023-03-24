"""empty message

Revision ID: ce8924880e88
Revises: 0f86706696fc
Create Date: 2023-03-24 12:30:44.339098

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce8924880e88'
down_revision = '0f86706696fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('coyote_map_images', sa.Column('imageName', sa.String(), nullable=False))
    op.add_column('coyote_map_images', sa.Column('imageRegion', sa.Integer(), nullable=False))
    op.add_column('coyote_map_images', sa.Column('imageUrl', sa.String(), nullable=False))
    op.drop_column('coyote_map_images', 'imageurl')
    op.drop_column('coyote_map_images', 'imageregion')
    op.drop_column('coyote_map_images', 'imagename')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('coyote_map_images', sa.Column('imagename', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('coyote_map_images', sa.Column('imageregion', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('coyote_map_images', sa.Column('imageurl', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('coyote_map_images', 'imageUrl')
    op.drop_column('coyote_map_images', 'imageRegion')
    op.drop_column('coyote_map_images', 'imageName')
    # ### end Alembic commands ###