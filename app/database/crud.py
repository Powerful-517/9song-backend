from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.models.user import User as UserModel
from app.models.song import Song as SongModel
from app.models.playlist import PlayList as PlayListModel
from app.models.playlistsong import PlayListSong as PlayListSongModel

from app.schemas.user import UserCreate as UserCreateSchema
from app.schemas.song import SongCreate as SongCreateSchema
from app.schemas.playlist import PlayListCreate as PlayListCreateSchema


def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()


def get_user_by_nickname(db: Session, nickname: str):
    return db.query(UserModel).filter(UserModel.nickname == nickname).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserModel).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreateSchema):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    hashed_password = pwd_context.hash(user.password)
    db_user = UserModel(username=user.username, nickname=user.nickname, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_song(db: Session, song_id: int):
    return db.query(SongModel).filter(SongModel.id == song_id).first()


def get_songs_by_uploader_id(db: Session, uploader_id: int, skip: int = 0, limit: int = 100):
    return db.query(SongModel).filter(SongModel.uploader_id == uploader_id).offset(skip).limit(limit).all()


def get_songs_by_playlist_id(db: Session, playlist_id: int, skip: int = 0, limit: int = 100):
    return db.query(SongModel).join(PlayListSongModel).filter(
        PlayListSongModel.playlist_id == playlist_id and PlayListSongModel.song_id == SongModel.id
    ).offset(skip).limit(limit).all()


def get_songs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SongModel).offset(skip).limit(limit).all()


def create_song(db: Session, song: SongCreateSchema, uploader_id: int):
    db_song = SongModel(name=song.name, artist=song.artist, album=song.album,
                        file_name=song.file_name, uploader_id=uploader_id)
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song


def get_playlist(db: Session, playlist_id: int):
    return db.query(PlayListModel).filter(PlayListModel.id == playlist_id).first()


def get_playlists_by_owner_id(db: Session, owner_id: int, skip: int = 0, limit: int = 100):
    return db.query(PlayListModel).filter(PlayListModel.owner_id == owner_id).offset(skip).limit(limit).all()


def get_playlists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PlayListModel).offset(skip).limit(limit).all()


def create_playlist(db: Session, playlist: PlayListCreateSchema, owner_id: int):
    db_playlist = PlayListModel(name=playlist.name, owner_id=owner_id)
    db.add(db_playlist)
    db.commit()
    db.refresh(db_playlist)
    return db_playlist


def update_playlist_cur_song(db: Session, playlist_id: int, song_id: int):
    db_playlist = db.query(PlayListModel).filter(PlayListModel.id == playlist_id).first()
    db_playlist.cur_song_id = song_id
    db.commit()
    db.refresh(db_playlist)
    return db_playlist


def create_playlist_song(db: Session, playlist_id: int, song_id: int):
    db_playlist_song = PlayListSongModel(playlist_id=playlist_id, song_id=song_id)
    db.add(db_playlist_song)
    db.commit()
    db.refresh(db_playlist_song)
    return db_playlist_song
