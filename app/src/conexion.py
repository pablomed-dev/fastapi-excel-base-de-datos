import pyodbc
from app.src.config import Config

class DbConexion:
    def __init__(self, config: Config):
        self.config = config
        self.conexion_str = None
        self.conexion = None

    def conectar_bd_academico(self):
              
        try:
            self.conexion_str = f"DSN={self.config.sybase_dsn_academico};UID={self.config.sybase_user_academico};PWD={self.config.sybase_password_academico}"
            self.conexion = pyodbc.connect(self.conexion_str)

            return self.conexion
        
        except Exception as e:
            raise ConnectionError(f"Error crítico al conectar a la base de datos: {str(e)}")

    def cerrar(self):
        if self.conexion:
            self.conexion.close()

    @property
    def dsn(self):
        return self.config.sybase_dsn_academico

    @property
    def usuario(self):
        return self.config.sybase_user_academico

    def autenticar_usuario_bd(self, usuario: str, password: str) -> bool:
        """
        Intenta conectar a SQL Anywhere 17 con el usuario y contraseña proporcionados.
        Retorna True si son válidos, False en caso contrario.
        """

        cadena_odbc = f"DSN= {self.config.sybase_dsn_academico};UID={usuario};PWD={password}"

        try:
            conexion = pyodbc.connect(cadena_odbc, timeout=10)

            # ¡Si llegó aquí, las credenciales son 100% correctas!
            # Cerramos la conexión inmediatamente (solo queríamos verificar)
            conexion.close()
            return True
        except pyodbc.Error as e:
            # SQL Anywhere devuelve error cuando UID o PWD son incorrectos
            # (Código de error SQL Anywhere: -103 'User ID or password is invalid')

            print(f"Error de autenticación para {usuario} - {self.config.sybase_dsn_academico} : {e}")
            return False