from modelos import Estudiante
from funcionesAuxiliares import mostrar_menu, validar_entero, validar_calificacion, buscar_estudiante

lista_estudiantes = []

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Nombre del estudiante: ")
            edad = validar_entero("Edad del estudiante: ")
            carrera = input("Carrera del estudiante: ")
            estudiante = Estudiante(nombre, edad, carrera)
            lista_estudiantes.append(estudiante)
            print(f"Estudiante {nombre} registrado exitosamente.")

        elif opcion == "2":
            nombre = input("Nombre del estudiante: ")
            estudiante = buscar_estudiante(nombre, lista_estudiantes)
            if estudiante:
                nota = validar_calificacion("Ingrese la calificación: ")
                estudiante.agregar_calificacion(nota)
                print("Calificación agregada correctamente.")
            else:
                print("Estudiante no encontrado.")

        elif opcion == "3":
            nombre = input("Nombre del estudiante: ")
            estudiante = buscar_estudiante(nombre, lista_estudiantes)
            if estudiante:
                estudiante.mostrar_info()
            else:
                print("Estudiante no encontrado.")

        elif opcion == "4":
            if lista_estudiantes:
                for estudiante in lista_estudiantes:
                    estudiante.mostrar_info()
                    print("--------------")
            else:
                print("No hay estudiantes registrados.")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    main()