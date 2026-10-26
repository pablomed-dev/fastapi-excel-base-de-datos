import jwt
import bcrypt
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from app.src.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

#Indica a FastApi que el token se obtiene en la ruta /auth/login
oauth2_scheme = OAuth2AuthorizationCodeBearer(tokenUrl= "auth/login")

# --- 1. GESTIÓN DE CONTRASEÑAS (BCRYPT) ---
def hashear_password(password: str) -> str:
    """Convierte texto plano en un hash seguro para guardar en la BD."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"),salt).decode("utf-8")

def verificar_password(password_plano: str, password_hasheado: str) -> bool:
    """Compara si la contraseña enviada coincide con el hash guardado"""
    return bcrypt.checkpw(
        password_plano.encode("utf-8"),
        password_hasheado.encode("utf-8")
    )