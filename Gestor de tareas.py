def Menu_Tareas():  # Función que imprime el menú de opciones
    print("\nMenu - Gestor de Tareas")
    print("1. Crear Tarea")
    print("2. Listar Tareas")
    print("3. Editar estado de tarea")
    print("4. Salir")

def opcion1():  # Función que permite agregar una tarea
    tarea = input("Ingrese la descripción de la tarea: ")
    with open("tareas.txt", "a") as file:  # Abre el archivo en modo agregar
        file.write(tarea + "\n")  # Guarda la tarea con un salto de línea
    print("Tarea agregada.\n")

def opcion2():  # Función que permite listar las tareas
    print("\nLista de Tareas:")
    try: 
        with open("tareas.txt", "r") as file:  # Abre el archivo en modo lectura
            tareas = file.readlines()  # Lee todas las líneas
            if not tareas:
                print("No hay tareas guardadas.\n")
                return
            for i, tarea in enumerate(tareas, 1):  # Enumera las tareas desde 1
                print(f"{i}. {tarea.strip()}")  # Muestra cada tarea sin espacios extra
    except FileNotFoundError:
        print("No hay tareas guardadas.\n")

def opcion3():  # Función que permite marcar una tarea como completada
    opcion2()  # Muestra la lista de tareas existentes
    try:
        tarea_num = int(input("\nIngrese el número de la tarea que desea marcar como completada: "))
        with open("tareas.txt", "r") as file:
            tareas = file.readlines()  # Obtiene todas las tareas
        if 0 < tarea_num <= len(tareas):  # Verifica que el número sea válido
            tareas.pop(tarea_num - 1)  # Elimina la tarea seleccionada
            with open("tareas.txt", "w") as file:  # Reescribe el archivo sin la tarea eliminada
                file.writelines(tareas)
            print("Tarea completada y eliminada.\n")
        else:
            print("Número de tarea inválido.\n")  # Si el número no está en el rango
    except ValueError:
        print("Debe ingresar un número válido.\n")
    except FileNotFoundError:
        print("No hay tareas guardadas.\n")

def main():  # Función principal
    while True:
        Menu_Tareas()
        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            opcion1()  # Agregar tarea
        elif opcion == '2':
            opcion2()  # Listar tareas
        elif opcion == '3':
            opcion3()  # Marcar tarea como completada
        elif opcion == '4':
            print("Saliendo...\n")
            break  # Sale del bucle y termina el programa
        else:
            print("Opción no válida, por favor intente de nuevo.\n")  # Control de errores

if __name__ == "__main__":  # Llamada a la función principal
    main()
    # Fin del archivo