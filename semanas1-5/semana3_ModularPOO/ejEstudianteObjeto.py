class Estudiante:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_atributos(self):
        return f"El estudiante {self.nombre} tiene una nota de {self.nota}"

    def calificacion(self):
        if int(self.nota) >= 70:
            return "aprobado"
        else: 
            return "reprobado"



estudiante = Estudiante("Fatima","71")

print(estudiante.mostrar_atributos())
print(estudiante.calificacion())
