"""
Módulo para resolución de colisiones por encadenamiento (chaining).
Utiliza defaultdict para simplificar la gestión de cubetas.
"""
from collections import defaultdict

class ChainingBuckets:
    def __init__(self, tamaño):
        # Cada índice tiene una lista de pares clave-valor
        self.tamaño = tamaño
        self.buckets = defaultdict(list)

    def insertar(self, idx, clave, valor):
        cubeta = self.buckets[idx]
        for i, (k, _) in enumerate(cubeta):
            if k == clave:
                cubeta[i] = (clave, valor)
                return False  # No se incrementa elementos
        cubeta.append((clave, valor))
        return True  # Se incrementa elementos

    def buscar(self, idx, clave):
        cubeta = self.buckets[idx]
        for k, v in cubeta:
            if k == clave:
                return v
        return None

    def __iter__(self):
        for cubeta in self.buckets.values():
            for par in cubeta:
                yield par
