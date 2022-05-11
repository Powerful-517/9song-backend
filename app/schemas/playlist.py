from pydantic import BaseModel
from .song import Song


# Pydantic PlayList model
class PlayListBase(BaseModel):
    name: str


class PlayListCreate(PlayListBase):
    pass


class PlayList(PlayListBase):
    id: int
    owner_id: int
    # songs: list[Song] = []

    class Config:
        orm_mode = True
