# Clase Estudiante que representa a un estudiante con sus datos y métodos relacionados
class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.calificaciones = []

    # Método para agregar una calificación válida al estudiante
    def agregar_calificacion(self, nota):
        if 0 <= nota <= 100:
            self.calificaciones.append(nota)
        else:
            print("La calificación debe estar entre 0 y 100.")

    # Método para calcular el promedio de calificaciones
    def promedio(self):
        if self.calificaciones:
            return sum(self.calificaciones) / len(self.calificaciones)
        else:
            return 0.0

    # Método para mostrar la información completa del estudiante
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Carrera: {self.carrera}")
        print(f"Calificaciones: {self.calificaciones}")
        print(f"Promedio: {self.promedio():.2f}")