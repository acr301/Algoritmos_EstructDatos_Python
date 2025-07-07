"""
Módulo para métodos de resolución de colisiones por direccionamiento abierto (open addressing).
Incluye: lineal, cuadrático, double hashing y soporte para agregar más.
"""
import random

class OpenAddressingProbe:
    def __init__(self, tamaño, metodo='lineal', hash_func=None, hash2_func=None):
        self.tamaño = tamaño
        self.metodo = metodo
        self.hash_func = hash_func if hash_func is not None else (lambda k, t: hash(k) % t)
        self.hash2_func = hash2_func if hash2_func is not None else (lambda k, t: 1 + (hash(k) % (t - 1)))

    def probe(self, clave):
        idx = self.hash_func(clave, self.tamaño)
        if self.metodo == 'lineal':
            for i in range(self.tamaño):
                yield (idx + i) % self.tamaño
        elif self.metodo == 'cuadratico':
            for i in range(self.tamaño):
                yield (idx + i * i) % self.tamaño
        elif self.metodo == 'double_hashing':
            step = self.hash2_func(clave, self.tamaño)
            for i in range(self.tamaño):
                yield (idx + i * step) % self.tamaño
        elif self.metodo == 'random':
            # Ejemplo: random probing (no recomendado en producción, pero útil para comparar)
            indices = list(range(self.tamaño))
            random.shuffle(indices)
            for i in indices:
                yield (idx + i) % self.tamaño
        else:
            raise ValueError('Método de sondeo no soportado')

# Ejemplo de uso:
# probe = OpenAddressingProbe(17, metodo='double_hashing')
# for pos in probe.probe('clave'): print(pos)
