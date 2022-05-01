from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from ..database.database import Base


class PlayListSong(Base):
    # This attribute tells SQLAlchemy the name of the table in database
    __tablename__ = "playlist_song"

    id = Column(Integer, primary_key=True, index=True)
    playlist_id = Column(Integer, ForeignKey("playlists.id"))
    song_id = Column(Integer, ForeignKey("songs.id"))

    playlists = relationship("PlayList", back_populates="playlist_songs")
    songs = relationship("Song", back_populates="playlist_songs")
