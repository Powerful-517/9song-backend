from pydantic import BaseModel
from .song import Song


# Pydantic PlayList model
class PlayListBase(BaseModel):
    name: str
    owner_id: int


class PlayListCreate(PlayListBase):
    pass


class PlayList(PlayListBase):
    id: int
    songs: list[Song] = []

    class Config:
        orm_mode = True
