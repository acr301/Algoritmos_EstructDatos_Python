import os
import sys

def listar_archivos_recursivo(ruta):
    """
    Lista todos los archivos y subdirectorios de manera recursiva,
    mostrando la estructura completa desde la ruta dada.

    Args:
        ruta (str): Ruta del directorio inicial (ej: "/home/usuario/proyectos").

    Estados:
        - Base: Cuando el elemento actual es un archivo (no hay más recursión).
        - Recursivo: Cuando el elemento es un directorio (se llama a sí mismo).
    """

    # Verificamos si la ruta existe
    if not os.path.exists(ruta):
        print(f"Error: La ruta '{ruta}' no existe.")
        return

    # Recorremos cada elemento en el directorio actual (incluyendo subdirectorios)
    # si se removiera el for, se detendria al encontrar un archivo del directorio actual, sin ir por los subdirectorios 
    # notese como se le pasa el "ruta" y luego hace ruta_completa equivalente al subdirectorio encontrado en ruta
    for nombre in os.listdir(ruta):
        ruta_completa = os.path.join(ruta, nombre)  # Ruta absoluta del elemento

        # --- Estado Base ---
        # Si es un archivo, lo imprimimos y terminamos la recursión para este elemento.
        if os.path.isfile(ruta_completa):
            print(f"Archivo: {ruta_completa}")

        # --- Estado Recursivo ---
        # Si es un directorio, lo imprimimos y llamamos a la función recursivamente.
        elif os.path.isdir(ruta_completa):
            print(f"Directorio: {ruta_completa}")
            listar_archivos_recursivo(ruta_completa)  # Llamada recursiva


# Codigo para correrlo desde la terminal pasando argumentos de sistema 
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: python3 {sys.argv[0]} <ruta_directorio>", file=sys.stderr)
        sys.exit(1)

    ruta = sys.argv[1]
    print(f"=== Iniciando búsqueda en: '{ruta}' ===")  # Debug
    listar_archivos_recursivo(ruta)
    print("=== Búsqueda finalizada ===")
