"""empty message

Revision ID: 0d850b77ddf0
Revises: 
Create Date: 2020-07-14 19:35:35.995492

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0d850b77ddf0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('familyMembers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('avatar', sa.Text(), nullable=True),
    sa.Column('photo', sa.Text(), nullable=True),
    sa.Column('parenty_id', sa.Integer(), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=True, auto_now_add=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.Column('created_by_user_id', sa.Integer(), nullable=False),
    sa.Column('isAdmin', sa.Boolean(), nullable=True),
    sa.Column('motivation_quote', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('username')
    )
    op.drop_index('email', table_name='familymembers')
    op.drop_index('name', table_name='familymembers')
    op.drop_index('username', table_name='familymembers')
    op.drop_table('familymembers')
    op.drop_table('objective')
    op.add_column('tasks', sa.Column('family_core_value', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'family_core_value')
    op.create_table('objective',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_by_user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('creation_date', mysql.DATETIME(), nullable=False),
    sa.Column('updated_date', mysql.DATETIME(), nullable=True),
    sa.Column('family_core_value', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('objective_type', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('description', mysql.TEXT(), nullable=False),
    sa.Column('target', mysql.TEXT(), nullable=False),
    sa.Column('kpi', mysql.TEXT(), nullable=True),
    sa.Column('target_date', mysql.DATETIME(), nullable=False),
    sa.Column('target_pingos', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('objective_status', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('objective_manual_progress', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('objective_calculated_progress', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('achievement_date', mysql.DATETIME(), nullable=True),
    sa.Column('manual_distributed_pingos', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('calculated_distributed_pingos', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['created_by_user_id'], ['users.id'], name='objective_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('familymembers',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('username', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('password', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('avatar', mysql.TEXT(), nullable=True),
    sa.Column('photo', mysql.TEXT(), nullable=True),
    sa.Column('parenty_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('creation_date', mysql.DATETIME(), nullable=True),
    sa.Column('updated_date', mysql.DATETIME(), nullable=True),
    sa.Column('created_by_user_id', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('isAdmin', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.Column('motivation_quote', mysql.TEXT(), nullable=True),
    sa.Column('description', mysql.TEXT(), nullable=True),
    sa.Column('status', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.CheckConstraint('(`isAdmin` in (0,1))', name='familymembers_chk_1'),
    sa.CheckConstraint('(`status` in (0,1))', name='familymembers_chk_2'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='familymembers_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('username', 'familymembers', ['username'], unique=True)
    op.create_index('name', 'familymembers', ['name'], unique=True)
    op.create_index('email', 'familymembers', ['email'], unique=True)
    op.drop_table('familyMembers')
    # ### end Alembic commands ###
