# API de Usuarios

## Descripción
API desarrollada con FastAPI para gestionar usuarios con operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

## Versión
1.0.0

## Requisitos
- Python 3.7+
- FastAPI
- Pydantic
- Email-validator

## Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/api-usuarios.git
cd api-usuarios

# Crear un entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install fastapi uvicorn pydantic email-validator

# Iniciar el servidor
uvicorn main:app --reload
```

## Modelo de Datos

### Usuario

| Campo   | Tipo     | Descripción                       | Restricciones                |
|---------|----------|-----------------------------------|------------------------------|
| id      | str      | ID único del usuario              | Generado automáticamente (UUID) |
| nombre  | str      | Nombre del usuario                | Longitud mínima: 2 caracteres |
| edad    | int      | Edad del usuario                  | Entre 1 y 119 años           |
| correo  | EmailStr | Correo electrónico del usuario    | Formato de email válido      |
| ciudad  | str      | Ciudad de residencia              | Longitud mínima: 2 caracteres |

## Endpoints

### Verificación del Servicio

```
GET /
```

**Respuesta de ejemplo:**
```json
{
  "message": "API de Usuarios funcionando correctamente",
  "timestamp": "2025-04-07T15:30:45.123456"
}
```

### Crear Usuario

```
POST /usuarios
```

**Cuerpo de la solicitud:**
```json
{
  "nombre": "Sara Maria",
  "edad": 25,
  "correo": "sara@gmail.com",
  "ciudad": "Medellín"
}
```

**Respuesta (código 201):**
```json
{
  "id": "7f9e1074-81a5-4a52-9f62-7358289c10a5",
  "nombre": "Sara Maria",
  "edad": 25,
  "correo": "sara@gmail.com",
  "ciudad": "Medellín"
}
```

### Obtener Todos los Usuarios

```
GET /usuarios
```

**Respuesta:**
```json
[
  {
    "id": "1",
    "nombre": "Maria",
    "edad": 25,
    "correo": "maria@gmail.com",
    "ciudad": "Medellín"
  },
  {
    "id": "2",
    "nombre": "Carlos",
    "edad": 30,
    "correo": "carlos@gmail.com",
    "ciudad": "Cali"
  }
  // ... más usuarios
]
```

### Obtener Usuario por ID

```
GET /usuarios/{usuario_id}
```

**Parámetros:**
- `usuario_id`: ID del usuario a obtener

**Respuesta:**
```json
{
  "id": "1",
  "nombre": "Maria",
  "edad": 25,
  "correo": "maria@gmail.com",
  "ciudad": "Medellín"
}
```

### Actualizar Usuario

```
PUT /usuarios/{user_id}
```

**Parámetros:**
- `user_id`: ID del usuario a actualizar

**Cuerpo de la solicitud:**
```json
{
  "id": "1",
  "nombre": "Maria Actualizada",
  "edad": 26,
  "correo": "maria.actualizada@gmail.com",
  "ciudad": "Bogotá"
}
```

**Respuesta:**
```json
{
  "id": "1",
  "nombre": "Maria Actualizada",
  "edad": 26,
  "correo": "maria.actualizada@gmail.com",
  "ciudad": "Bogotá"
}
```

### Eliminar Usuario

```
DELETE /usuarios/{user_id}
```

**Parámetros:**
- `user_id`: ID del usuario a eliminar

**Respuesta:**
```json
{
  "id": "1",
  "nombre": "Maria",
  "edad": 25,
  "correo": "maria@gmail.com",
  "ciudad": "Medellín"
}
```

## Códigos de Estado

| Código | Descripción            | Contexto                                      |
|--------|------------------------|-----------------------------------------------|
| 200    | OK                     | Solicitud exitosa                             |
| 201    | Created                | Usuario creado correctamente                  |
| 400    | Bad Request            | ID de usuario ya existe                       |
| 404    | Not Found              | Usuario no encontrado                         |
| 422    | Unprocessable Entity   | Datos inválidos en la solicitud               |

## Documentación Interactiva

FastAPI proporciona documentación interactiva automática. Para acceder a ella:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Notas de Implementación

- La API utiliza una lista en memoria para almacenar los usuarios. En un entorno de producción, se recomienda utilizar una base de datos.
- Los IDs de los usuarios están preestablecidos para los datos de ejemplo, pero los nuevos usuarios reciben UUIDs generados automáticamente.
- La validación de datos se realiza mediante Pydantic.

## Ejemplo de Uso con Curl

```bash
# Verificar el estado de la API
curl -X GET http://localhost:8000/

# Crear un nuevo usuario
curl -X POST http://localhost:8000/usuarios \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Nuevo Usuario", "edad": 35, "correo": "nuevo@gmail.com", "ciudad": "Bogotá"}'

# Obtener todos los usuarios
curl -X GET http://localhost:8000/usuarios

# Obtener un usuario específico
curl -X GET http://localhost:8000/usuarios/1

# Actualizar un usuario
curl -X PUT http://localhost:8000/usuarios/1 \
  -H "Content-Type: application/json" \
  -d '{"id": "1", "nombre": "Nombre Actualizado", "edad": 26, "correo": "actualizado@gmail.com", "ciudad": "Bogotá"}'

# Eliminar un usuario
curl -X DELETE http://localhost:8000/usuarios/1
```

## Licencia
[Especifica tu licencia aquí, por ejemplo: MIT, Apache 2.0, etc.]
