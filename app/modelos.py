from typing import Any

def crear_tarea(nombre: str, **kwargs: Any) -> dict:
    """Crea una tarea pendiente con metadatos opcionales permitidos."""

    if not nombre.strip():
        raise ValueError("El nombre de la tarea no puede estar vacío")

    campos_permitidos = {"prioridad", "etiqueta", "fecha_limite"}

    for campo in kwargs:
        if campo not in campos_permitidos:
            raise ValueError(f"Campo no permitido: {campo}")

    tarea = {"nombre": nombre,"completada": False}
    tarea.update(kwargs)

    return tarea