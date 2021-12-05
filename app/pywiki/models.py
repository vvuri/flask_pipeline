from sqlalchemy import Boolean, Column, Integer, String, Text, DateTime, ForeignKey, MetaData
# from sqlalchemy.orm import relationship

from database import Base
import re

# from sqlalchemy.orm import declarative_base
# Base = declarative_base()

# https://alembic.sqlalchemy.org/en/latest/naming.html
convention = {
  "ix": "ix_%(column_0_label)s",
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    text = Column(Text(255))
    created_at = Column(DateTime)
    is_public = Column(Boolean, default=True)
    slug = Column(String(128), unique=True)

    tag_id = Column(Integer, ForeignKey('tag.id'))

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.slug = generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Post id:{}, title: {}, slug: {}>'.format(self.id, self.title, self.slug)


class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64))
