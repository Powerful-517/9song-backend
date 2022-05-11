from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import database, crud
from app.schemas.user import User
from app.utils.auth import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[
        Depends(get_current_user),
    ],
    responses={
        404: {"description": "Not found"},
    },
)


@router.get("/", response_model=list[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
