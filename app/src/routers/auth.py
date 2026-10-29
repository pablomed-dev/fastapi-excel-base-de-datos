from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.src.seguridad import verificar_password, hashear_password, crear_token_acceso

router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"]
)

# NOTA: Aquí deberías consultar a tu repositorio/base de datos Sybase
# Este es un usuario de ejemplo para que puedas probar inmediatamente:
USUARIO_DE_PRUEBA = {
    "usuario": "admin",
    # Este hash corresponde a la contraseña: "password123"
    "password_hash": hashear_password("admin123")
}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint para iniciar sesión.
    Recibe 'username' y 'password' (form-data).
    """

    # 1. Validar que el usuario exista (aquí llamarías a tu bd)
    if form_data.username != USUARIO_DE_PRUEBA["usuario"]:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos"
        )

    # 2. Validar que la contraseña coincida
    if not verificar_password(form_data.password, USUARIO_DE_PRUEBA["password_hash"]):
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos"
        )

    # 3. Crear y retornar el token JWT
    token_jwt = crear_token_acceso(datos={"sub": form_data.username})

    return {
        "access_token": token_jwt,
        "token_type": "bearer"
    }
    