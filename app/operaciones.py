from typing import Any
from app.modelos import crear_tarea

def agregar_tarea(tareas: list[dict], nombre: str, **kwargs: Any) -> dict:
    """Crea una tarea y la agrega a la lista recibida."""
    nueva_tarea = crear_tarea(nombre, **kwargs)

    tareas.append(nueva_tarea)

    return nueva_tarea

def listar_pendientes(tareas: list[dict]) -> list[dict]:
    """Devuelve las tareas que todavía no se han completado."""
    pendientes = []

    for tarea in tareas:
        if tarea["completada"] == False:
            pendientes.append(tarea)

    return pendientes

def buscar_tareas(tareas: list[dict], palabra: str) -> list[dict]:
    """Busca tareas cuyo nombre contenga la palabra indicada."""
    resultados = []

    for tarea in tareas:
        if palabra.lower() in tarea["nombre"].lower():
            resultados.append(tarea)

    return resultados
