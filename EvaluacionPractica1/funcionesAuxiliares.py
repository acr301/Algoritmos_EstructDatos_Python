# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Registrar nuevo estudiante")
    print("2. Agregar calificación a un estudiante")
    print("3. Mostrar información de un estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Salir")

# Función para validar que la entrada sea un número entero positivo
def validar_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Por favor, ingresa un número entero positivo.")
        except ValueError:
            print("Entrada no válida. Ingresa un número entero.")

# Función para validar calificación entre 0 y 100
def validar_calificacion(mensaje):
    while True:
        try:
            calificacion = float(input(mensaje))
            if 0 <= calificacion <= 100:
                return calificacion
            else:
                print("La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada no válida. Ingresa un número.")

# Función para buscar un estudiante por nombre en la lista de estudiantes
def buscar_estudiante(nombre, lista_estudiantes):
    for estudiante in lista_estudiantes:
        if estudiante.nombre.lower() == nombre.lower():
            return estudiante
    return None