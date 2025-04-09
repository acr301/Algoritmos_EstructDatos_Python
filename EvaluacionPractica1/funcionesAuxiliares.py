def mostrar_menu():
    print(f"""
        ---Menu de opciones---
    1. Registrar nuevo estudiante 
    2. Agregar calificación a un estudiante
    3. Mostrar información de un estudiante
    4. Mostrar todos los estudiantes
    5. Salir del programa
          """)

def menu_seleccion():
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("Por favor, ingrese un número entre 1 y 5.")
        except ValueError:
            print("Entrada no válida. Ingrese un número.")

def validar_edad(mensaje):
    """
    Solicita al usuario un número entero positivo.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("Debe ser un número entero positivo.")
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")

def validar_calificacion(mensaje):
    """
    Solicita al usuario una calificación válida entre 0 y 100.
    """
    while True:
        try:
            nota = float(input(mensaje))
            if 0 <= nota <= 100:
                return nota
            else:
                print("La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada no válida. Ingrese un número.")

def validar_string(mensaje):
    """
    Solicita al usuario un string de texto que no este vacía
    """
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        else:
            print("Este campo no puede estar vacío.")

def buscar_estudiante(nombre, lista_estudiantes):
    """
    Busca un estudiante por nombre en una lista. Devuelve el estudiante si lo encuentra, o None si no.
     """
    for estudiante in lista_estudiantes:
        if estudiante.nombre.lower() == nombre.lower():
            return estudiante

    return None
