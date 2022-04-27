from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from ..database.database import Base


class PlayListSong(Base):
    # This attribute tells SQLAlchemy the name of the table in database
    __tablename__ = "playlist_song"

    id = Column(Integer, primary_key=True, index=True)
    playlist_id = Column(Integer, ForeignKey("playlists.id"))
    song_id = Column(Integer, ForeignKey("songs.id"))

    playlist = relationship("PlayList", back_populates="PlayListSong")
    song = relationship("Song", back_populates="PlayListSong")
