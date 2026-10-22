# 🚀 API RESTful para Procesamiento e Inserción de Datos Excel (FastAPI)

API Backend desarrollada en Python con FastAPI para la lectura, validación y persistencia masiva de registros desde archivos Excel hacia una base de datos relacional.

## 📌 Descripción del Proyecto

Este proyecto surge para automatizar la ingesta y estructuración de datos provenientes de planillas Excel (`.xlsx`), procesando los registros en memoria para su posterior inserción y almacenamiento persistente en base de datos.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python
* **Framework Backend:** FastAPI
* **Procesamiento de Datos:** Pandas
* **Servidor ASGI:** Uvicorn
* **Base de Datos:** Sql anywhere

## ✨ Funcionalidades Actuales

* 📥 **Carga de Archivos:** Endpoint HTTP POST optimizado para recibir archivos `.xlsx`.
* 🔄 **Procesamiento e Ingesta:** Lectura y estructuración automatizada de filas y columnas en memoria.
* 💾 **Persistencia:** Mapeo e inserción de registros procesados dentro de la base de datos relacional.
* 📑 **Documentación Automática:** Interfaz interactiva para pruebas mediante Swagger UI (`/docs`) y ReDoc (`/redoc`).

## ⚙️ Instalación y Ejecución Local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/pablomed-dev/fastapi-excel-base-de-datos.git
   cd fastapi-excel-base-de-datos
   ```

2. **Crear y activar un entorno virtual:**
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

4. **Levantar el servidor de desarrollo:**
```bash
uvicorn main:app --reload
# O
uvicorn app.main:app --reload
```

5. **Acceder a la documentación interactiva en el navegador:**  http://127.0.0.1:8000/docs

## 🚀 Próximas Mejoras (Roadmap de Desarrollo)
Entendiendo la evolución de la arquitectura para un entorno de producción, las siguientes iteraciones del proyecto incluirán:

- [ ] **Autenticación y Autorización:** Implementación de seguridad con tokens JWT (OAuth2).
    
- [ ] **Validación de Datos:** Enriquecimiento de esquemas con Pydantic para un control riguroso de tipos y capturas de excepciones.
    
- [ ] **Contenerización:** Creación de `Dockerfile` y `docker-compose.yml` para facilitar el despliegue de la API y la base de datos.
    
- [ ] **Pruebas Automatizadas:** Incorporación de tests unitarios y de integración con `pytest`.
    
- [ ] **Procesamiento Asíncrono:** Gestión de archivos pesados en segundo plano para optimizar los tiempos de respuesta HTTP.
