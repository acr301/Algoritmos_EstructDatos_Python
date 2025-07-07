"""
Datasets sugeridos para benchmarking de tablas hash.
Incluye casos típicos y adversos para evaluar dispersión y colisiones.
"""
import random
import string

def dataset_aleatorio(n, clave_len=8):
    """Claves aleatorias de longitud fija, valores enteros."""
    return [("".join(random.choices(string.ascii_letters, k=clave_len)), i) for i in range(n)]

def dataset_secuencial(n):
    """Claves y valores enteros secuenciales."""
    return [(i, i) for i in range(n)]

def dataset_colisiones(n, tamaño_tabla):
    """Claves diseñadas para colisionar en la misma posición (para hash simple)."""
    base = "A"
    return [(base * ((i % tamaño_tabla) + 1), i) for i in range(n)]

def dataset_palabras_comunes():
    """Palabras comunes en español como claves."""
    palabras = [
        "casa", "perro", "gato", "sol", "luna", "agua", "fuego", "tierra", "aire", "mar",
        "libro", "mesa", "silla", "puerta", "ventana", "flor", "árbol", "cielo", "estrella", "nube"
    ]
    return [(p, i) for i, p in enumerate(palabras)]

# Ejemplo de uso:
# ds = dataset_aleatorio(1000)
# ds = dataset_secuencial(1000)
# ds = dataset_colisiones(1000, 10)
# ds = dataset_palabras_comunes()
