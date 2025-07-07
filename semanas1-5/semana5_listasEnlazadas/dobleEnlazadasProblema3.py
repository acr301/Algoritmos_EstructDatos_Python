"""
Sistema de gestión de pacientes para clínica usando lista doblemente enlazada.
Permite agregar pacientes, mostrar orden de atención por prioridad y eliminar pacientes atendidos.
"""

import os
# colorama lo instale con pip3 install colorama
from colorama import init, Fore, Back, Style

# Inicializar colorama
init(autoreset=True)
# el autoreset permite que se reestablezca al texto predeterminado cada vez

# clase con propiedades del Paciente, asi como sus enlaces al anterior y al siguiente
class NodoPaciente:
    def __init__(self, nombre, edad, sintoma, prioridad):
        self.nombre = nombre
        self.edad = edad
        self.sintoma = sintoma
        self.prioridad = prioridad
        self.siguiente = None
        self.anterior = None

# ListaPacientes que contiene una coleccion de NodoPaciente
class ListaPacientes:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        
    def esta_vacia(self):
        return self.cabeza is None
    
    def agregar_paciente(self, nombre, edad, sintoma, prioridad):
        nuevo_paciente = NodoPaciente(nombre, edad, sintoma, prioridad)
        
        if self.esta_vacia():
            self.cabeza = nuevo_paciente
            self.cola = nuevo_paciente
        else:
            # Insertar ordenado por prioridad (1 es máxima prioridad)
            actual = self.cabeza
            anterior = None
            
            while actual is not None and actual.prioridad <= nuevo_paciente.prioridad:
                anterior = actual
                actual = actual.siguiente
            
            if anterior is None:
                # Insertar al inicio
                nuevo_paciente.siguiente = self.cabeza
                self.cabeza.anterior = nuevo_paciente
                self.cabeza = nuevo_paciente
            elif actual is None:
                # Insertar al final
                nuevo_paciente.anterior = self.cola
                self.cola.siguiente = nuevo_paciente
                self.cola = nuevo_paciente
            else:
                # Insertar en medio
                anterior.siguiente = nuevo_paciente
                nuevo_paciente.anterior = anterior
                nuevo_paciente.siguiente = actual
                actual.anterior = nuevo_paciente
    
    def eliminar_paciente(self, nombre):
        if self.esta_vacia():
            return False
        
        actual = self.cabeza
        
        while actual is not None:
            if actual.nombre == nombre:
                if actual.anterior is None:
                    # Es el primer nodo
                    self.cabeza = actual.siguiente
                    if self.cabeza is not None:
                        self.cabeza.anterior = None
                    else:
                        self.cola = None
                elif actual.siguiente is None:
                    # Es el último nodo
                    self.cola = actual.anterior
                    self.cola.siguiente = None
                else:
                    # Está en medio
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                return True
            actual = actual.siguiente
        
        return False
    
    def mostrar_pacientes(self):
        if self.esta_vacia():
            print(Fore.YELLOW + "No hay pacientes en espera.")
            return
        
        print(Fore.CYAN + "\n--- ORDEN DE ATENCIÓN ---")
        print(Fore.CYAN + "(Prioridad 1 es máxima, 5 es mínima)\n")
        
        actual = self.cabeza
        posicion = 1
        
        while actual is not None:
            # Asignar color según prioridad
            if actual.prioridad == 1:
                color = Fore.RED + Back.WHITE + Style.BRIGHT
            elif actual.prioridad == 2:
                color = Fore.MAGENTA + Style.BRIGHT
            elif actual.prioridad == 3:
                color = Fore.YELLOW
            elif actual.prioridad == 4:
                color = Fore.GREEN
            else:
                color = Fore.BLUE
            
            print(f"{color}[P{actual.prioridad}] {posicion}. {actual.nombre} ({actual.edad} años)")
            print(f"   Síntoma: {actual.sintoma}")
            print(Style.RESET_ALL)
            
            actual = actual.siguiente
            posicion += 1
    
    def longitud(self):
        contador = 0
        actual = self.cabeza
        
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        
        return contador

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print(Fore.CYAN + "\n--- SISTEMA DE GESTIÓN DE PACIENTES ---")
    print(Fore.GREEN + "1. Agregar nuevo paciente")
    print(Fore.GREEN + "2. Mostrar orden de atención")
    print(Fore.GREEN + "3. Atender paciente (eliminar del sistema)")
    print(Fore.GREEN + "4. Mostrar cantidad de pacientes en espera")
    print(Fore.RED + "5. Salir")
    print(Style.RESET_ALL)

def main():
    lista_pacientes = ListaPacientes()
    
    while True:
        mostrar_menu()
        opcion = input(Fore.YELLOW + "Seleccione una opción: " + Style.RESET_ALL)
        
        if opcion == "1":
            limpiar_consola()
            print(Fore.CYAN + "\n--- REGISTRAR NUEVO PACIENTE ---\n")
            
            nombre = input("Nombre completo: ")
            edad = input("Edad: ")
            sintoma = input("Síntoma principal: ")
            
            while True:
                prioridad = input("Prioridad (1-5, donde 1 es máxima): ")
                if prioridad.isdigit() and 1 <= int(prioridad) <= 5:
                    prioridad = int(prioridad)
                    break
                print(Fore.RED + "Error: La prioridad debe ser un número entre 1 y 5")
            
            lista_pacientes.agregar_paciente(nombre, edad, sintoma, prioridad)
            print(Fore.GREEN + f"\nPaciente {nombre} registrado con éxito!")
            
        elif opcion == "2":
            limpiar_consola()
            lista_pacientes.mostrar_pacientes()
            
        elif opcion == "3":
            limpiar_consola()
            if lista_pacientes.esta_vacia():
                print(Fore.YELLOW + "No hay pacientes para atender.")
            else:
                print(Fore.CYAN + "\n--- ATENDER PACIENTE ---\n")
                lista_pacientes.mostrar_pacientes()
                nombre = input("\nIngrese el nombre del paciente a atender: ")
                
                if lista_pacientes.eliminar_paciente(nombre):
                    print(Fore.GREEN + f"\nPaciente {nombre} atendido y eliminado del sistema.")
                else:
                    print(Fore.RED + f"\nNo se encontró un paciente con el nombre {nombre}.")
            
        elif opcion == "4":
            limpiar_consola()
            print(Fore.CYAN + f"\nPacientes en espera: {lista_pacientes.longitud()}")
            
        elif opcion == "5":
            print(Fore.CYAN + "\nSaliendo del sistema...")
            break
            
        else:
            print(Fore.RED + "\nOpción no válida. Por favor intente nuevamente.")
            
        input("\nPresione Enter para continuar...")
        limpiar_consola()

if __name__ == "__main__":
    limpiar_consola()
    main()
