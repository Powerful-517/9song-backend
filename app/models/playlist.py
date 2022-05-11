from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from ..database.database import Base


class PlayList(Base):
    # This attribute tells SQLAlchemy the name of the table in database
    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    cur_song_id = Column(Integer, ForeignKey("songs.id"))
    cur_update_time = Column(DateTime, onupdate=func.now())

    owner = relationship("User", back_populates="playlists")
    playlist_songs = relationship("PlayListSong", back_populates="playlists")
