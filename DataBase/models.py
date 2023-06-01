from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, mapped_column
from DataBase.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    ip_address = Column(String, unique=True, nullable=False)
    images = relationship("Image", back_populates="user", lazy="joined")


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)
    path_image = Column(String, nullable=False)
    description = Column(String, nullable=True)
    user_id = mapped_column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="images")
