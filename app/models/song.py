from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database.database import Base


class Song(Base):
    # This attribute tells SQLAlchemy the name of the table in database
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    artist = Column(String)
    album = Column(String)
    uploader_id = Column(Integer, ForeignKey("users.id"))
    file_name = Column(String)

    uploader = relationship("User", back_populates="songs")
    playlist_songs = relationship("PlayListSong", back_populates="songs")
