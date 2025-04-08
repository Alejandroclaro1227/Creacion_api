from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import List
from uuid import uuid4
from datetime import datetime

# inicialización de la aplicación FastAPI
app = FastAPI(
    title="API de Usuarios",
    description="API para gestionar usuarios con operaciones CRUD",
    version="1.0.0"
)

class Usuario(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), description="ID único del usuario")
    nombre: str = Field(..., description="Nombre del usuario", min_length=2)
    edad: int = Field(..., description="Edad del usuario", gt=0, lt=120)
    correo: EmailStr = Field(..., description="Correo del usuario", min_length=2)
    ciudad: str = Field(..., description="Ciudad de residencia", min_length=2)

    class Config:
        """Configuración extra para el modelo"""
        schema_extra = {
            "example": {
                "id": "7f9e1074-81a5-4a52-9f62-7358289c10a5",
                "nombre": "Sara Maria",
                "edad": 25,
                "correo": "sara@gmail.com",
                "ciudad": "Medellín"
            }
        }

# Lista de usuarios (con UUID generado por defecto)
list_usuarios: List[Usuario] = [
    Usuario(id="1", nombre="Maria", edad=25, ciudad="Medellín", correo="maria@gmail.com"),
    Usuario(id="2", nombre="Carlos", edad=30, ciudad="Cali", correo="carlos@gmail.com"),
    Usuario(id="3", nombre="Sofia", edad=22, ciudad="Cartagena", correo="sofia@gmail.com"),
    Usuario(id="4", nombre="Andres", edad=28, ciudad="Barranquilla", correo="andres@gmail.com"),
    Usuario(id="5", nombre="Lucia", edad=27, ciudad="Pereira", correo="lucia@gmail.com"),
    Usuario(id="6", nombre="Diego", edad=24, ciudad="Santa Marta", correo="diego@gmail.com"),
]

@app.get("/")
async def root():
    return {
        "message": "API de Usuarios funcionando correctamente",
        "timestamp": datetime.now().isoformat()
    }

@app.post("/usuarios", response_model=Usuario, status_code=201)
async def crear_usuario(usuario: Usuario):
    """
    Endpoint para crear un nuevo usuario.
    Args:
        usuario (Usuario): Datos del nuevo usuario.
    Returns:
        Usuario: Usuario creado.
    """
    # Verificar si el ID ya existe
    if any(u.id == usuario.id for u in list_usuarios):
        raise HTTPException(status_code=400, detail="El ID del usuario ya existe")
    
    list_usuarios.append(usuario)
    print("Se ha creado un nuevo usuario correctamente.")
    return usuario

@app.get("/usuarios", response_model=List[Usuario])
async def obtener_usuarios():
    """
    Endpoint para obtener la lista de usuarios.
    Returns:
        List[Usuario]: Lista de usuarios.
    """
    return list_usuarios

@app.get("/usuarios/{usuario_id}", response_model=Usuario)
async def obtener_usuario(usuario_id: str):
    """
    Endpoint para obtener un usuario por su ID.
    Args:
        usuario_id (str): ID del usuario.
    Returns:
        Usuario: Usuario encontrado.
    Raises:
        HTTPException: Si el usuario no se encuentra.
    """
    for usuario in list_usuarios:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.put("/usuarios/{user_id}", response_model=Usuario)
async def actualizar_usuario(user_id: str, usuario_actualizado: Usuario):
    """
    Endpoint para actualizar un usuario existente.
    Args:
        user_id (str): ID del usuario a actualizar.
        usuario_actualizado (Usuario): Datos del usuario con los nuevos valores.
    Returns:
        Usuario: Usuario actualizado.
    """
    for index, usuario in enumerate(list_usuarios):
        if usuario.id == user_id:
            list_usuarios[index] = usuario_actualizado  # Actualizar los datos del usuario
            print(f"Usuario con ID {user_id} actualizado correctamente.")
            return usuario_actualizado  # Retornar el usuario actualizado
    
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

@app.delete("/usuarios/{user_id}", response_model=Usuario)
async def eliminar_usuario(user_id: str):
    """
    Endpoint para eliminar un usuario por su ID.
    Args:
        user_id (str): ID del usuario a eliminar.
    Returns:
        Usuario: Usuario eliminado.
    """
    for index, usuario in enumerate(list_usuarios):
        if usuario.id == user_id:
            eliminado = list_usuarios.pop(index)  # Eliminar el usuario de la lista
            print(f"Usuario con ID {user_id} eliminado correctamente.")
            return eliminado  # Retornar el usuario eliminado
    
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
