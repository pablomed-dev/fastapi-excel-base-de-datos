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
