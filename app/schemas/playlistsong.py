from pydantic import BaseModel


# Pydantic PlayListSong model
class PlayListSongBase(BaseModel):
    song_id: int
    playlist_id: int


class PlayListSongCreate(PlayListSongBase):
    pass


class PlayListSong(PlayListSongBase):
    id: int

    class Config:
        orm_mode = True
