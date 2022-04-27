from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import database, crud
from app.schemas.user import User, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(database.get_db)):
    db_user_by_username = crud.get_user_by_username(db, username=user.username)
    if db_user_by_username:
        raise HTTPException(status_code=400, detail="User name already registered")
    db_user_by_nickname = crud.get_user_by_nickname(db, nickname=user.nickname)
    if db_user_by_nickname:
        raise HTTPException(status_code=400, detail="User nickname already registered")
    return crud.create_user(db=db, user=user)
