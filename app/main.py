from fastapi import FastAPI

from app.database import database

# Create the database tables
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello 9song!"}
