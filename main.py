from colorama import Fore, Style, init
from app.operaciones import agregar_tarea, listar_pendientes, buscar_tareas

def mostrar_menu() -> None:
    print("\n===== GESTOR DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Listar tareas pendientes")
    print("3. Buscar tareas")
    print("4. Salir")

def mostrar_tareas(tareas: list[dict]) -> None:
    """Muestra las tareas con sus prioridades y etiquetas."""
    for numero, tarea in enumerate(tareas, start=1):
        nombre = tarea["nombre"]
        prioridad = tarea.get("prioridad", "")
        etiqueta = tarea.get("etiqueta", "")

        if prioridad.lower() == "alta":
            color = Fore.RED
        elif prioridad.lower() == "media":
            color = Fore.YELLOW
        elif prioridad.lower() == "baja":
            color = Fore.GREEN
        else:
            color = Fore.WHITE

        texto = f"{numero}. {nombre}"

        if prioridad:
            texto += f" {color}[{prioridad}]{Style.RESET_ALL}"
        if etiqueta:
            texto += f" {Fore.CYAN}[{etiqueta}]{Style.RESET_ALL}"
        print(texto)


def solicitar_prioridad() -> str:
    """Solicita y valida una prioridad opcional."""
    prioridades_validas = ("alta", "media", "baja")

    while True:
        prioridad = input(
            "Prioridad (Alta, Media, Baja) o Enter para omitir: "
        ).strip().lower()

        if prioridad == "":
            return ""

        if prioridad in prioridades_validas:
            return prioridad.capitalize()

        print(Fore.RED + "Prioridad no válida. Inténtalo nuevamente.")

def main() -> None:
    init(autoreset=True)
    tareas = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Introduce el nombre de la tarea: ").strip()
            if not nombre:
                print("El nombre de la tarea no puede estar vacío.")
            else:
                prioridad = solicitar_prioridad()
                etiqueta = input("Introduce una etiqueta o Enter para omitir: ").strip()
                datos_opcionales = {}
                if prioridad:
                    datos_opcionales["prioridad"] = prioridad
                if etiqueta:
                    datos_opcionales["etiqueta"] = etiqueta
                nueva_tarea = agregar_tarea(
                    tareas,
                    nombre,
                    **datos_opcionales
                )
                print(f"Tarea '{nueva_tarea['nombre']}' agregada correctamente.")

        elif opcion == "2":
            pendientes = listar_pendientes(tareas)
            if len(pendientes) == 0:
                print("No hay tareas pendientes.")
            else:
                print("\n===== TAREAS PENDIENTES =====")
                mostrar_tareas(pendientes)

        elif opcion == "3":
            palabra = input("Introduce una palabra para buscar: ")
            resultados = buscar_tareas(tareas, palabra)
            if len(resultados) == 0:
                print("No se encontraron tareas.")
            else:
                print("\n===== RESULTADOS DE BÚSQUEDA =====")
                mostrar_tareas(resultados)

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Inténtalo nuevamente.")


if __name__ == "__main__":
    main()