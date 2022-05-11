from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import database, crud
from app.schemas.song import Song, SongCreate
from app.schemas.user import User
from app.utils.auth import get_current_user
from app.utils.oss import *

router = APIRouter(
    prefix="/songs",
    tags=["songs"],
    dependencies=[
        Depends(get_current_user),
    ],
    responses={
        404: {"description": "Not found"},
    },
)


@router.get("/", response_model=list[Song])
def read_songs(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    songs = crud.get_songs(db, skip=skip, limit=limit)
    return songs


@router.get("/uploader_id/{uploader_id}", response_model=list[Song])
def read_songs_by_uploader_id(uploader_id: int, skip: int = 0, limit: int = 100,
                              db: Session = Depends(database.get_db)):
    songs = crud.get_songs_by_uploader_id(db, skip=skip, limit=limit, uploader_id=uploader_id)
    return songs


@router.get("/playlist_id/{playlist_id}", response_model=list[Song])
def read_songs_by_playlist_id(playlist_id: int, skip: int = 0, limit: int = 100,
                              db: Session = Depends(database.get_db)):
    songs = crud.get_songs_by_playlist_id(db, skip=skip, limit=limit, playlist_id=playlist_id)
    return songs


@router.get("/upload_url")
def get_song_upload_url(file_name: str):
    if is_file_exists(file_name):
        raise HTTPException(
            status_code=409,
            detail="File already exists."
        )
    return {"upload_url": get_upload_url(file_name)}


@router.get("/download_url")
def get_song_download_url(file_name: str):
    if not is_file_exists(file_name):
        raise HTTPException(
            status_code=404,
            detail="File not found."
        )
    return {"download_url": get_download_url(file_name)}


@router.post("/", response_model=Song)
def create_song(song: SongCreate, db: Session = Depends(database.get_db), user: User = Depends(get_current_user)):
    file_name = song.file_name
    # Client should firstly upload the song file
    if not is_file_exists(file_name):
        raise HTTPException(
            status_code=404,
            detail="File not found."
        )
    return crud.create_song(db, song=song, uploader_id=user.id)
