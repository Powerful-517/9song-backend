from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import database, crud
from app.schemas.playlist import PlayList, PlayListCreate
from app.schemas.playlistsong import PlayListSong
from app.schemas.user import User
from app.utils.auth import get_current_user

router = APIRouter(
    prefix="/playlists",
    tags=["playlists"],
    dependencies=[
        Depends(get_current_user),
    ],
    responses={
        404: {"description": "Not found"},
    },
)


@router.get("/", response_model=list[PlayList])
def read_playlists(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    playlists = crud.get_playlists(db, skip=skip, limit=limit)
    return playlists


@router.get("/{playlist_id}", response_model=PlayList)
def read_playlists(playlist_id: int, db: Session = Depends(database.get_db)):
    playlist = crud.get_playlist(db, playlist_id=playlist_id)
    return playlist


@router.get("/owner_id/{owner_id}", response_model=list[PlayList])
def read_playlists(owner_id: int, skip: int = 0, limit: int = 100,
                   db: Session = Depends(database.get_db)):
    playlists = crud.get_playlists_by_owner_id(db, owner_id=owner_id, skip=skip, limit=limit)
    return playlists


@router.post("/", response_model=PlayList)
def create_playlist(playlist: PlayListCreate, db: Session = Depends(database.get_db),
                    user: User = Depends(get_current_user)):
    owner_id = user.id
    return crud.create_playlist(db, playlist=playlist, owner_id=owner_id)


# Add a song to a playlist
@router.post("/add_song/{playlist_id}/{song_id}", response_model=PlayListSong)
def create_playlist_song(playlist_id: int, song_id: int, db: Session = Depends(database.get_db)):
    return crud.create_playlist_song(db, playlist_id=playlist_id, song_id=song_id)
