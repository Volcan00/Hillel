"""second

Revision ID: 339ed7bfc498
Revises: 0742979dc25f
Create Date: 2023-03-08 16:41:31.981933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '339ed7bfc498'
down_revision = '0742979dc25f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'currency', ['id'])
    op.create_unique_constraint(None, 'users', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'currency', type_='unique')
    # ### end Alembic commands ###
