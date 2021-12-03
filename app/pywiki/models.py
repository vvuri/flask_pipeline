from sqlalchemy import Boolean, Column, Integer, String, Text, DateTime, ForeignKey, MetaData
# from sqlalchemy.orm import relationship
from database import Base

# https://alembic.sqlalchemy.org/en/latest/naming.html
convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': (
        'fk__%(table_name)s__%(all_column_names)s__'
        '%(referred_table_name)s'
    ),
    'pk': 'pk__%(table_name)s'
}

# Registry for all tables
metadata = MetaData(naming_convention=convention)


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    text = Column(Text(255))
    created_at = Column(DateTime)
    is_public = Column(Boolean, default=True)

    tag_id = Column(Integer, ForeignKey('tag.id'))


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64))
