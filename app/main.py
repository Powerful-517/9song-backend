from fastapi import FastAPI

from app.database import database

from app.routers import users, token, register, songs, playlists

# Create the database tables
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(token.router)
app.include_router(register.router)
app.include_router(songs.router)
app.include_router(playlists.router)


@app.get("/")
async def root():
    return {"message": "Hello 9song!"}
