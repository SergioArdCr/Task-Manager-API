"""inicial

Revision ID: 55f75d237950
Revises: 
Create Date: 2026-04-22 22:29:40.689509

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55f75d237950'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('usuarios',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('username', sa.String(), nullable=True),
        sa.Column('password', sa.String(), nullable=True),
        sa.Column('rol', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proyectos',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('nombre', sa.String(), nullable=True),
        sa.Column('descripcion', sa.String(), nullable=True),
        sa.Column('owner_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['owner_id'], ['usuarios.id']),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proyecto_miembros',
        sa.Column('usuario_id', sa.Integer(), nullable=True),
        sa.Column('proyecto_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['proyecto_id'], ['proyectos.id']),
        sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'])
    )
    op.create_table('tareas',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('titulo', sa.String(), nullable=True),
        sa.Column('descripcion', sa.String(), nullable=True),
        sa.Column('estado', sa.String(), nullable=True),
        sa.Column('prioridad', sa.String(), nullable=True),
        sa.Column('proyecto_id', sa.Integer(), nullable=True),
        sa.Column('asignado_a', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['asignado_a'], ['usuarios.id']),
        sa.ForeignKeyConstraint(['proyecto_id'], ['proyectos.id']),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    op.drop_table('tareas')
    op.drop_table('proyecto_miembros')
    op.drop_table('proyectos')
    op.drop_table('usuarios')
