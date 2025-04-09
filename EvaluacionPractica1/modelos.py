from funcionesAuxiliares import validar_calificacion

class Estudiante:
    def __init__(self, nombre, edad, carrera, calificaciones=None):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
                         # que sea una sola calificacion, si ES QUE HAY una, si no, (varias) una lista
        self.calificaciones = calificaciones if calificaciones is not None else []

    def agregar_calificacion(self, nota):
        nota_validada = validar_calificacion(nota)

        # si de verdad hay una nota_validada
        if nota_validada is not None:
            self.calificaciones.append(nota_validada)
            print(f"Nota {nota_validada} agregada a {self.nombre}.")


# RegistroEstudiantes tiene (contiene objetos Estudiante)
#
class RegistroEstudiantes:
    def __init__(self):
        # es decir, esta es una lista de objetos de la clase Estudiante
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
