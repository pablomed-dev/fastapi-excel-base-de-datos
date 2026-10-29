import jwt
import bcrypt
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.src.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

#Indica a FastApi que el token se obtiene en la ruta /auth/login
oauth2_scheme = OAuth2PasswordBearer(tokenUrl= "/auth/login")

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

# --- 2. GESTIÓN DE TOCKENS JWT ---
def crear_token_acceso(datos: dict) -> str:
    """Generar un JWT firmado con tiempo de expiración"""
    a_codificar = datos.copy()
    expiracion = datetime.now(timezone.utc) + timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    a_codificar.update({"exp": expiracion})

    return jwt.encode(a_codificar, SECRET_KEY, algorithm= ALGORITHM)

# --- 3. DEPENDENCIA PARA PROTEGER RUTAS ---
def obtener_usuario_actual(token: str = Depends(oauth2_scheme)) -> str:
    """
        Se ejecuta automaticamente en rutas protegidas.
        Verifica que el token sea válido y no haya expirado.
    """

    error_autenticacion = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido o expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try :
        payload = jwt.decode(token, SECRET_KEY, algorithms = [ALGORITHM])
        usuario: str = payload.get("sub") # sub guarda el identificador del usuario
        if usuario is None:
            raise error_autenticacion
        return usuario
    except jwt.PyJWTError:
        raise error_autenticacion