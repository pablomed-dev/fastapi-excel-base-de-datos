import pandas as pd
from io import BytesIO
from app.src.repositorios.repositorio_procesar_excel_dnerhs import repositorio_procesar_excel_dnerhs
from app.src.config import configuraciones
from app.src.conexion import DbConexion

class servicio_procesar_excel_dnerhs():
    def __init__(self, p_archivo_excel):
        self.archivo_excel = p_archivo_excel

    def get_detalle_excel(self):
        # Leer todas las hojas - devuelve un diccionario {nombre_hoja: dataframe}
        df_excel = pd.read_excel(BytesIO(self.archivo_excel), sheet_name=None)
        
        """for hoja, df in df_excel.items():
            print(f"\n Hoja: '{hoja}'")
            print(f" -Filas: {len(df)}")
            print(f" -Columnas: {list(df.columns)}")
            print(f" -Dimensiones: {df.shape}")
            print(df)
            print("------------------------------------------")"""

        return {
            "total_hojas": len(df_excel),
            "hojas": list(df_excel.keys()),
            "contenido": { nombre: df.to_string() for nombre, df in df_excel.items() }
        }

    def guardar(self):
        conexion_bd = DbConexion(configuraciones)
        repositorio_excel = repositorio_procesar_excel_dnerhs(self.archivo_excel, conexion_bd)

        return repositorio_excel.guardar()

        