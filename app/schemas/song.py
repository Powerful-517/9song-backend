from pydantic import BaseModel


# Pydantic Song model
class SongBase(BaseModel):
    name: str
    artist: str
    album: str
    uploader_id: int


class SongCreate(SongBase):
    file: bytes


class Song(SongBase):
    id: int
    file_url: str

    class Config:
        orm_mode = True
