from pydantic import BaseModel
from .song import Song
from .playlist import PlayList


# Pydantic User model
class UserBase(BaseModel):
    username: str
    nickname: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    songs: list[Song] = []
    playlists: list[PlayList] = []

    class Config:
        orm_mode = True
