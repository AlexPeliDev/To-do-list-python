import json
import os

ARCHIVO = "tareas.json"


def cargar_tareas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_tareas(tareas):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(tareas, f, ensure_ascii=False, indent=4)


def mostrar_tareas(tareas):
    if not tareas:
        print("\nNo hay tareas.\n")
        return

    print("\n--- LISTA DE TAREAS ---")
    for i, tarea in enumerate(tareas, start=1):
        estado = "✅" if tarea["completada"] else "❌"
        print(f"{i}. {tarea['texto']} [{estado}]")
    print()


def agregar_tarea(tareas):
    texto = input("Escribe la nueva tarea: ").strip()
    if texto:
        tareas.append({"texto": texto, "completada": False})
        guardar_tareas(tareas)
        print("Tarea añadida.\n")
    else:
        print("No puedes añadir una tarea vacía.\n")


def completar_tarea(tareas):
    mostrar_tareas(tareas)
    if not tareas:
        return

    try:
        num = int(input("Número de la tarea completada: "))
        if 1 <= num <= len(tareas):
            tareas[num - 1]["completada"] = True
            guardar_tareas(tareas)
            print("Tarea marcada como completada.\n")
        else:
            print("Número inválido.\n")
    except ValueError:
        print("Debes escribir un número.\n")


def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    if not tareas:
        return

    try:
        num = int(input("Número de la tarea que quieres eliminar: "))
        if 1 <= num <= len(tareas):
            borrada = tareas.pop(num - 1)
            guardar_tareas(tareas)
            print(f"Tarea eliminada: {borrada['texto']}\n")
        else:
            print("Número inválido.\n")
    except ValueError:
        print("Debes escribir un número.\n")


def menu():
    tareas = cargar_tareas()

    while True:
        print("=== TO-DO LIST ===")
        print("1. Ver tareas")
        print("2. Añadir tarea")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            mostrar_tareas(tareas)
        elif opcion == "2":
            agregar_tarea(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.\n")


menu()









































