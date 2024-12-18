"""Add Product Table

Revision ID: 0b3348501057
Revises: 
Create Date: 2024-12-09 22:22:17.013370

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b3348501057'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('image_thumbnail', sa.String(length=255), nullable=True),
    sa.Column('image_mobile', sa.String(length=255), nullable=True),
    sa.Column('image_tablet', sa.String(length=255), nullable=True),
    sa.Column('image_desktop', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###
