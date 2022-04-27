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
    file_url = Column(String)
    uploader_id = Column(Integer, ForeignKey("users.id"))

    uploader = relationship("User", back_populates="songs")
