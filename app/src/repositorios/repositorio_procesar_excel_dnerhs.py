import pandas as pd
from io import BytesIO
#from fastapi import HTTPException

class repositorio_procesar_excel_dnerhs():
    def __init__(self, archivo_excel, conexion_bd):
        self.archivo_excel = archivo_excel
        self.conexion_bd = conexion_bd

    def guardar(self):
        if self.conexion_bd is None:
            #raise HTTPException(status_code=500, detail="No se pudo establecer la conexión con la base de datos")
            raise ConnectionError("No se pudo establecer la conexión con la base de datos")


        if not self.archivo_excel or not self.conexion_bd :
            return None
        
        #conectar con la base de datos
        conexion = self.conexion_bd.conectar_bd_academico()
        if not conexion:
            raise ConnectionError("La base de datos rechazó la conexión")
        
        cursor = conexion.cursor()
        #Activar optimización para sybase para buen rendimiento
        cursor.fast_executemany = True

        #Crear dataframe del archivo excel
        df_excel = pd.read_excel(BytesIO(self.archivo_excel), sheet_name=None)
        filas_totales = 0

        try:
            for nombre_hoja, df_hoja in df_excel.items():
                df_hoja = df_hoja.where(pd.notnull(df_hoja), None)
                datos = [tuple(row) for row in df_hoja.to_numpy()]
                query = "INSERT INTO Bases_id (idobd, Nombre_base, Descripción) VALUES(?,?,?)"

                print(f"Insertando {len(datos)} filas en {nombre_hoja}...")
                cursor.executemany(query, datos)
                filas_totales += len(datos)

            conexion.commit()

        except Exception as e:
            conexion.rollback()
            # Excepción nativa de Python
            raise RuntimeError(f"Error al insertar datos en la BD: {str(e)}")
            
        finally:
            # Ojo: se cierra al final de todo el bucle
            cursor.close()
            conexion.close()

        return {"mensaje": f"Procesadas {filas_totales} filas totales"}