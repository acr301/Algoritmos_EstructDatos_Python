"""
TablaHashIterable: tabla hash académica y flexible para pruebas y benchmarks.
- Permite ajustar función hash, tamaño de tabla y método de colisiones (chaining u open addressing lineal).
- Implementa métodos insertar, buscar y es iterable sobre los pares clave-valor.
"""

from resolucion_colisiones_direccionamiento import OpenAddressingProbe
from resolucion_colisiones_encadenamiento import ChainingBuckets
import math

def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def siguiente_primo(n):
    while True:
        n += 1
        if es_primo(n):
            return n

def es_potencia_de_2(n):
    return n > 0 and (n & (n - 1)) == 0

class TablaHashIterable:
    def __init__(self, tamaño=8, hash_func=None, metodo_colision='chaining', metodo_sondeo='lineal', hash2_func=None, factor_carga_max=0.7):
        """
        metodo_colision: 'chaining' o 'open_addressing'
        metodo_sondeo: 'lineal', 'cuadratico', 'double_hashing', 'random' (solo para open addressing)
        hash2_func: función hash secundaria para double hashing
        factor_carga_max: umbral para redimensionar automáticamente
        """
        self.tamaño = tamaño
        self.hash_func = hash_func if hash_func is not None else lambda k, t: hash(k) % t
        self.metodo_colision = metodo_colision
        self.metodo_sondeo = metodo_sondeo
        self.hash2_func = hash2_func if hash2_func is not None else (lambda k, t: 1 + (hash(k) % (t - 1)))
        self.elementos = 0
        self.factor_carga_max = factor_carga_max
        if metodo_colision == 'chaining':
            self.tabla = ChainingBuckets(tamaño)
        elif metodo_colision == 'open_addressing':
            self.tabla = [None for _ in range(tamaño)]
            self.probe = OpenAddressingProbe(tamaño, metodo=metodo_sondeo, hash_func=self.hash_func, hash2_func=self.hash2_func)
        else:
            raise ValueError('Método de colisión no soportado')

    def insertar(self, clave, valor):
        # Redimensionar si el factor de carga supera el umbral
        if self.factor_carga() > self.factor_carga_max:
            if self.metodo_colision == 'chaining' or self.metodo_sondeo in ['lineal', 'cuadratico', 'random']:
                # Para hash modular, usar siguiente primo
                nuevo_tam = siguiente_primo(self.tamaño * 2)
            elif self.metodo_sondeo == 'double_hashing':
                # Para double hashing, preferible tamaño primo
                nuevo_tam = siguiente_primo(self.tamaño * 2)
            elif es_potencia_de_2(self.tamaño):
                nuevo_tam = self.tamaño * 2
            else:
                nuevo_tam = self.tamaño * 2
            self._redimensionar(nuevo_tam)
        idx = self.hash_func(clave, self.tamaño)
        if self.metodo_colision == 'chaining':
            if self.tabla.insertar(idx, clave, valor):
                self.elementos += 1
        elif self.metodo_colision == 'open_addressing':
            for pos in self.probe.probe(clave):
                if self.tabla[pos] is None or self.tabla[pos][0] == clave:
                    self.tabla[pos] = (clave, valor)
                    self.elementos += 1
                    return
            raise RuntimeError('Tabla llena (open addressing)')

    def buscar(self, clave):
        idx = self.hash_func(clave, self.tamaño)
        if self.metodo_colision == 'chaining':
            return self.tabla.buscar(idx, clave)
        elif self.metodo_colision == 'open_addressing':
            for pos in self.probe.probe(clave):
                par = self.tabla[pos]
                if par is None:
                    return None
                if par[0] == clave:
                    return par[1]
            return None

    def factor_carga(self):
        return self.elementos / self.tamaño

    def _redimensionar(self, nuevo_tamaño):
        # Decisión de diseño: se re-crea la tabla y se re-hashean todos los elementos
        elementos = list(self)
        self.tamaño = nuevo_tamaño
        if self.metodo_colision == 'chaining':
            self.tabla = ChainingBuckets(nuevo_tamaño)
        elif self.metodo_colision == 'open_addressing':
            self.tabla = [None for _ in range(nuevo_tamaño)]
            self.probe = OpenAddressingProbe(nuevo_tamaño, metodo=self.metodo_sondeo, hash_func=self.hash_func, hash2_func=self.hash2_func)
        self.elementos = 0
        for k, v in elementos:
            # Inserta sin volver a redimensionar recursivamente
            idx = self.hash_func(k, self.tamaño)
            if self.metodo_colision == 'chaining':
                self.tabla.insertar(idx, k, v)
                self.elementos += 1
            elif self.metodo_colision == 'open_addressing':
                for pos in self.probe.probe(k):
                    if self.tabla[pos] is None:
                        self.tabla[pos] = (k, v)
                        self.elementos += 1
                        break

    def __iter__(self):
        if self.metodo_colision == 'chaining':
            yield from self.tabla
        elif self.metodo_colision == 'open_addressing':
            for par in self.tabla:
                if par is not None:
                    yield par
