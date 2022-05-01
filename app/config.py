# The URL of the SQLite database file
SQLALCHEMY_DATABASE_URL = "sqlite:///app/database/app.db"

# Secret key for JWT token signing, you can generate one by execute "openssl rand -hex 32"
# Be sure to change it in production environment!
SECRET_KEY = ""

# JWT token sign algorithm
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 300
