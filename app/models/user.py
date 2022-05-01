from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..database.database import Base


class User(Base):
    # This attribute tells SQLAlchemy the name of the table in database
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    nickname = Column(String, unique=True)
    hashed_password = Column(String)

    songs = relationship("Song", back_populates="uploader")
    playlists = relationship("PlayList", back_populates="owner")
