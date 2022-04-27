from pydantic import BaseModel
from .song import Song
from .playlist import PlayList


# Pydantic User model
class UserBase(BaseModel):
    nickname: str


class UserCreate(UserBase):
    hashed_password: str


class User(UserBase):
    id: int
    songs: list[Song] = []
    playlists: list[PlayList] = []

    class Config:
        orm_mode = True
