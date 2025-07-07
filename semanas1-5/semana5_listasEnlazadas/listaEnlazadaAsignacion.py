"""
o	Leer los datos que se insertarán en la lista.
o	Implementar inserción al inicio.
o	Agregar método longitudLista() que cuente los nodos.
o	Método para determinar si la lista está vacía.
o	Agregar método que imprima el último valor de la lista.
"""


# Nodo individual
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.referencia = None 

# Coleccion/Contenedor de Nodos (lista enlazada)
class ListaEnlazada:
    def __init__(self, head=None):
        self.head = head

    # insercion al inicio
    def agregar(self, nuevo_nodo):

        # creamos un objeto actual para no perder la referencia al primer nodo 
        actual = self.head 

        if actual: # si el primer nodo existe 
            while actual.referencia: # mientras haya una referencia en dicho nodo (no es tail)
                actual = actual.referencia # asignamos una referencia distinta a None 

                # el bucle rompe cuando finalmente llegamos a uno cuya referencia sea None (tail)
            actual.referencia = nuevo_nodo # y entonces a ese ultimo elemento (tail) asignamos el nuevo nodo.
        else:
            self.head = nuevo_nodo # si no existe (lista vacia), directamente hacemos el nuevo nodo el head. 

    
    # esta funcion es lo mismo (un actual para no perder la referencia), sin embargo,
    # itera hasta que encuentre el valor dado 

    def eliminar(self, valor):

        actual = self.head

        if actual.valor == valor: # si el valor es el del nodo head 
            self.head = actual.referencia # entonces, hacemos del head la referencia (el nodo siguiente, el segundo)

        else: # cualquier otro nodo 
            while actual:
                if actual.valor == valor: # si encuentra el valor buscado
                    break # deja de buscar (rompe el bucle)

                # convierte un anterior en actual, que sera una referencia para que no
                # perdamos el hilo al eliminar el actual 
                anterior = actual 

                # lo enlaza 
                actual = actual.referencia

        
            if actual == None: # si el nodo a eliminar es el tail, no tenemos que preocuparnos por referencias  
                return 


            anterior.referencia = actual.referencia # movemos el enlace del que eliminaremos al que esta antes,
            actual = None # para poder eliminarlo sin perder el hilo.


    def insertar(self, nuevo_elemento, posicion):
        contador = 1
        actual = self.head

        if posicion == 1: # si insertamos un nodo head 
            nuevo_elemento.referencia = self.head
            self.head = nuevo_elemento


        while actual: # si no es head, iteramos
            if contador+1 == posicion: # si estamos justo una posicion antes de en la que queremos insertar 
                nuevo_elemento.referencia = actual.referencia # guardamos el enlace del que le precede 
                actual.referencia = nuevo_elemento # y hacemos que apunte al que insertamos
                return
            else: # si no, seguimos buscando
                contador += 1
                actual = actual.referencia


    # aprovechando las strings, con tal que haya una referencia ira apuntando al siguiente nodo con ->
    # y rompera el bucle con un ultimo -> a None
    def print(self):
        actual = self.head
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.referencia
        print("None")

    # itera como tantos nodos haya hasta llegar al cuya referencia es None
    def longitudLista(self):
        contador = 0
        actual = self.head
        while actual:
            contador += 1
            actual = actual.referencia
        return contador

    def estaVacia(self): # sencillo metodo con operador de identidad para ver si, al pasar la lista, no hay ninguna direccion a esta (mas bien a None).
        # o sea no hay ni siquiera un head
        return self.head is None


    def ultimoValor(self):
        actual = self.head
        if not actual:
            return None # no hay nodo ultimo, esta vacia
        while actual.referencia:
            actual = actual.referencia
        return actual.valor # rompe el bucle cuando ya no haya referencias, retorna el valor del ultimo

def menu():

    #instanciamos la clase ListaEnlazada
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

            #instanciamos un nodo 
            nuevo_nodo = Nodo(valor)

            #lo agregamos a la instancia de ListaEnlazada
            lista.agregar(nuevo_nodo)
            print(f"Nodo con valor '{valor}' agregado al final.")
        

        # creo que el resto se explican solos. 
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
