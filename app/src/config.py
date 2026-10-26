import os
from dotenv import load_dotenv

class Config():
    # Cargar variables del .env
    load_dotenv()

    # Obtener variables
    sybase_host = os.getenv("SYBASE_HOST")
    sybase_port = os.getenv("SYBASE_PORT")

    sybase_database_academico = os.getenv("SYBASE_DATABASE_ACADEMICO")
    sybase_user_academico = os.getenv("SYBASE_USER_ACADEMICO")
    sybase_password_academico = os.getenv("SYBASE_PASSWORD_ACADEMICO")
    sybase_dsn_academico = os.getenv("SYBASE_DSN_ACADEMICO")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

CORS_ORIGIN = [
    "http://localhost:5173",   # Frontend local (Vite)
    "http://127.0.0.1:8000",
]


configuraciones = Config()