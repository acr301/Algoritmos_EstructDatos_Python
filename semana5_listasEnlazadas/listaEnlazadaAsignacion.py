"""
o	Leer los datos que se insertarán en la lista.
o	Implementar inserción al inicio.
o	Agregar método longitudLista() que cuente los nodos.
o	Método para determinar si la lista está vacía.
o	Agregar método que imprima el último valor de la lista.
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.referencia = None 

class ListaEnlazada:
    def __init__(self, head=None):
        self.head = head

    def agregar(self, nuevo_nodo):
        actual = self.head
        if actual:
            while actual.referencia:
                actual = actual.referencia
            actual.referencia = nuevo_nodo
        else:
            self.head = nuevo_nodo

    def eliminar(self, valor):
        actual = self.head
        if actual.valor == valor:
            self.head = actual.referencia
        else:
            while actual:
                if actual.valor == valor:
                    break
                anterior = actual
                actual = actual.referencia 
            if actual == None:
                return
            anterior.referencia = actual.referencia
            actual = None

    def insertar(self, nuevo_elemento, posicion):
        contador = 1
        actual = self.head
        if posicion == 1:
            nuevo_elemento.referencia = self.head
            self.head = nuevo_elemento
        while actual:
            if contador+1 == posicion:
                nuevo_elemento.referencia = actual.referencia
                actual.referencia = nuevo_elemento
                return
            else:
                contador += 1
                actual = actual.referencia

    def print(self):
        actual = self.head
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.referencia
        print("None")

    def longitudLista(self):
        contador = 0
        actual = self.head
        while actual:
            contador += 1
            actual = actual.referencia
        return contador

    def estaVacia(self):
        return self.head is None

    def ultimoValor(self):
        actual = self.head
        if not actual:
            return None
        while actual.referencia:
            actual = actual.referencia
        return actual.valor

def menu():
    lista = ListaEnlazada()
    
    while True:
        print("\n--- MENÚ LISTA ENLAZADA ---")
        print("1. Agregar nodo al final")
        print("2. Insertar nodo en posición específica")
        print("3. Eliminar nodo por valor")
        print("4. Imprimir la lista")
        print("5. Mostrar longitud de la lista")
        print("6. Verificar si la lista está vacía")
        print("7. Mostrar último valor de la lista")
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            valor = input("Ingrese el valor del nuevo nodo: ")
            nuevo_nodo = Nodo(valor)
            lista.agregar(nuevo_nodo)
            print(f"Nodo con valor '{valor}' agregado al final.")
        
        elif opcion == "2":
            if lista.estaVacia():
                print("La lista está vacía, se agregará como primer elemento.")
                valor = input("Ingrese el valor del nuevo nodo: ")
                nuevo_nodo = Nodo(valor)
                lista.agregar(nuevo_nodo)
            else:
                lista.print()
                valor = input("Ingrese el valor del nuevo nodo: ")
                posicion = int(input(f"Ingrese la posición (1-{lista.longitudLista()+1}): "))
                if posicion < 1 or posicion > lista.longitudLista()+1:
                    print("Posición inválida!")
                    continue
                nuevo_nodo = Nodo(valor)
                lista.insertar(nuevo_nodo, posicion)
                print(f"Nodo con valor '{valor}' insertado en posición {posicion}.")
        
        elif opcion == "3":
            if lista.estaVacia():
                print("La lista está vacía, no hay nada que eliminar.")
            else:
                lista.print()
                valor = input("Ingrese el valor del nodo a eliminar: ")
                lista.eliminar(valor)
                print(f"Nodo con valor '{valor}' eliminado si existía.")
        
        elif opcion == "4":
            if lista.estaVacia():
                print("La lista está vacía.")
            else:
                print("Lista actual:")
                lista.print()
        
        elif opcion == "5":
            print(f"Longitud de la lista: {lista.longitudLista()}")
        
        elif opcion == "6":
            if lista.estaVacia():
                print("La lista está vacía.")
            else:
                print("La lista NO está vacía.")
        
        elif opcion == "7":
            ultimo = lista.ultimoValor()
            if ultimo is None:
                print("La lista está vacía.")
            else:
                print(f"Último valor de la lista: {ultimo}")
        
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()