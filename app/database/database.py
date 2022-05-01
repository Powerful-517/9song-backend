from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import SQLALCHEMY_DATABASE_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# This instance will be the actual database session
# Distinguish this instance from the `Session` importing from SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# The base class of the ORM models
Base = declarative_base()


# Give an independent session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        # Close it once the request is finished
        db.close()
