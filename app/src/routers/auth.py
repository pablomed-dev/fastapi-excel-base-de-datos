from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.src.config import configuraciones
from app.src.conexion import DbConexion
from app.src.seguridad import crear_token_acceso

router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"]
)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint para iniciar sesión.
    Recibe 'username' y 'password' (form-data).
    """

    gestor_conexion = DbConexion(configuraciones)

    # 1. Intentamos conectar a la bd con las credenciales ingresadas
    es_valido = gestor_conexion.autenticar_usuario_bd(
        usuario = form_data.username,
        password = form_data.password
    )
    
    # 2. Si falló la conexión por usuario/password incorrectos
    if not es_valido:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrecto",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # 3. Si tuvo éxito, generamos el jwt con el usuario de Sybase en 'sub'
    token_jwt = crear_token_acceso(datos={"sub": form_data.username})

    return {
        "access_token": token_jwt,
        "token_type": "bearer"
    }
    