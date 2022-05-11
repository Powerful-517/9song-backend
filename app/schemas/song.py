from pydantic import BaseModel


# Pydantic Song model
class SongBase(BaseModel):
    name: str
    artist: str
    album: str
    file_name: str


class SongCreate(SongBase):
    pass


class Song(SongBase):
    id: int
    uploader_id: int

    class Config:
        orm_mode = True
