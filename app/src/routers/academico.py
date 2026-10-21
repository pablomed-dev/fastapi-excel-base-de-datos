from fastapi import APIRouter, HTTPException, UploadFile, File
from app.src.config import configuraciones
from app.src.conexion import DbConexion
from app.src.servicios.servicio_procesar_excel_dnerhs import servicio_procesar_excel_dnerhs

router = APIRouter(
    prefix="/academico",
    tags=["Académico"]
)

#------------------------------------------------------------------------------------------------------------------------
@router.get("/prueba_conexion")
async def prueba(): 
    conexion_sybase = DbConexion(configuraciones)
    conexion = conexion_sybase.conectar_bd_academico()

    if conexion is None:
        raise HTTPException(status_code=500, detail="No se pudo establecer la conexión con la base de datos")

    try:
        cursor = conexion.cursor()
        query = "select number(*) as fila, * from sedes where idobd = 1 and estado = 'A'"
        cursor.execute(query)
        
        # Verificar si hay resultados
        columnas = [col[0] for col in cursor.description]
        rows = cursor.fetchall()
        
        # Convertir a diccionarios
        resultados = [dict(zip(columnas, row)) for row in rows]
        return resultados

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al consultar: {str(e)}")
    finally:
        conexion_sybase.cerrar()
        print(conexion_sybase.dsn)

#------------------------------------------------------------------------------------------------------------------------
@router.post("/detalles_excel_dnerhs")
async def detalles_excel_dnerhs(archivo: UploadFile = File(...)):
    """Endpoint para procesar archivo excel de la dnerhs"""    
    
    #validar que sea un archivo excel
    if not archivo.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(status_code=400, detail="El archivo debe ser Excel (.xlsx, .xls)")
    
    try:
        #Leer el contendio del archivo
        contenido_excel = await archivo.read()

        #Crear el objeto que gestionará el excel
        gestor_excel = servicio_procesar_excel_dnerhs(contenido_excel)
        #return {"mensaje":f"{gestor_excel.get_detalle_excel()}"}
        return {
            "status_code": 200,
            "detail": "ok",
            "data": gestor_excel.get_detalle_excel()
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al leer el contenido del archivo Excel: {str(e)}")

#------------------------------------------------------------------------------------------------------------------------
@router.post("/procesar_excel_dnerhs")
async def procesar_excel_dnerhs(archivo: UploadFile = File(...)):
    """Endpoint para procesar archivo excel de la dnerhs"""    
    
    #validar que sea un archivo excel
    if not archivo.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(status_code=400, detail="El archivo debe ser Excel (.xlsx, .xls)")
    
    try:
        #Leer el contendio del archivo
        contenido_excel = await archivo.read()

        #Crear el objeto que gestionará el excel
        gestor_excel = servicio_procesar_excel_dnerhs(contenido_excel)
        return gestor_excel.guardar()

    # Si fue un error de conexión a la BD -> 503 (Servicio no disponible)
    except ConnectionError as e:
        raise HTTPException(status_code=503, detail=str(e))

    # Si fue un error ejecutando la consulta -> 500 (Error interno)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Para cualquier otro error 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}") 