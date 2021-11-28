from sqlalchemy import Boolean, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship

# from .database import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    text = Column(Text(255))
    created_at = Column(DateTime)
    is_public = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")