from app.modelos import crear_tarea
from app.operaciones import agregar_tarea, listar_pendientes, buscar_tareas


def probar_gestor() -> None:
    """Comprueba las operaciones principales del gestor."""
    tareas = []

    # Prueba 1: Crear y agregar tareas
    agregar_tarea(tareas, "Estudiar Python", prioridad="Alta")
    agregar_tarea(tareas, "Comprar comida")
    agregar_tarea(tareas, "Terminar proyecto Python")

    assert len(tareas) == 3

    # Prueba 2: Listar pendientes
    tareas[1]["completada"] = True

    pendientes = listar_pendientes(tareas)

    assert len(pendientes) == 2

    # Prueba 3: Buscar tareas
    resultados = buscar_tareas(tareas, "python")

    assert len(resultados) == 2

    # Prueba 4: Validar campos opcionales
    try:
        crear_tarea("Nueva tarea", completada=True)
    except ValueError:
        pass
    else:
        raise AssertionError("Se esperaba un ValueError")

    # Prueba 5: Rechazar nombres vacíos
    try:
        crear_tarea("   ")
    except ValueError:
        pass
    else:
        raise AssertionError("Se esperaba un ValueError")

    print("¡Todas las pruebas se completaron correctamente!")


if __name__ == "__main__":
    probar_gestor()
