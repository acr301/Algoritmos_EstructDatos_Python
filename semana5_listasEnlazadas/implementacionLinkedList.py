class Nodo:

    # para facilidad asume un nodo unico head o un nodo tail
    # Lista vacia (Nodo unico)[Valor][None]
    # Lista para Nodo n (Nodo)[Valor][direccion distinta a None]
    # Lista (Nodos) (Tail)[Valor][None]

    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self, cabeza, cabeza_valor):

        # cabeza, primer Nodo, apunta a nada, lista vacia por defecto 
        
        self.cabeza = cabeza
        self.cabeza_valor = cabeza_valor

    def esta_vacia(self):
        # regresara True mientras sea None 
        return self.cabeza is None

    def insertar(self, valor):

        nuevo = Nodo(valor)

        if self.esta_vacia():
            self.cabeza_valor = nuevo

        else:
            actual = self.cabeza
            while actual.siguiente is not None:  # Verificamos explícitamente
                actual = actual.siguiente
            actual.siguiente = nuevo

    def eliminar(self, valor):
        if self.esta_vacia():  # Lista vacía
            return False

        actual = self.cabeza
        anterior = None

        while actual is not None:  # Verificación explícita
            if actual.valor == valor:
                if anterior is None:  # Es el primer nodo
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar(self, valor):
        actual = self.cabeza
        while actual is not None:  # Verificación explícita
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def imprimir(self):
        if self.esta_vacia():
            print("La lista está vacía")
            return

        actual = self.cabeza
        print("Lista enlazada:", end=" ")
        while actual is not None:  # Verificación explícita
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    # Métodos adicionales solicitados
    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def longitud_lista(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

    def ultimo_valor(self):
        if self.esta_vaca():
            return None
            
        actual = self.cabeza
        while actual.siguiente is not None:
            actual = actual.siguiente
        return actual.valor
