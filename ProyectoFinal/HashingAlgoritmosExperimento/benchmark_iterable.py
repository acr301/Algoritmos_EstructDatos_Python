"""
Benchmark académico flexible usando TablaHashIterable.
- Permite ajustar función hash, tamaño de tabla y método de colisiones.
- Solo mide tiempo de búsqueda (lookup).
- Exporta resultados a CSV.
"""

import timeit
import csv

# Benchmark académico para comparar tablas hash con diferentes métodos de colisión y datasets.
# Refactorizado para mayor claridad y análisis didáctico.

from tabla_hash_iterable import TablaHashIterable
from datasets_benchmark import dataset_aleatorio, dataset_secuencial, dataset_colisiones, dataset_palabras_comunes

# Parámetros de prueba
CANTIDADES = [100, 500, 1000, 5000, 10000]
REPS = {100: 50, 500: 20, 1000: 10, 5000: 5, 10000: 3}
METODOS_COLISION = ['chaining', 'open_addressing']
TAMANIOS_TABLA = [100, 500, 1000, 5000, 10000]

# Datasets para distintos escenarios
DATASETS = [
    (lambda n, t: dataset_aleatorio(n), 'aleatorio'),
    (lambda n, t: dataset_secuencial(n), 'secuencial'),
    (lambda n, t: dataset_colisiones(n, t), 'colisiones'),
    (lambda n, t: dataset_palabras_comunes(), 'palabras_comunes'),
]




def benchmark_tabla_busqueda(n, reps, claves, valores, metodo_colision, tamaño):
    """
    Inserta y busca todos los elementos, mide tiempo total y factor de carga final.
    """
    factor_carga_final = None
    tamaño_final = None
    def test():
        nonlocal factor_carga_final, tamaño_final
        t = TablaHashIterable(tamaño=tamaño, metodo_colision=metodo_colision)
        for k, v in zip(claves, valores):
            t.insertar(k, v)
        for k in claves:
            _ = t.buscar(k)
        factor_carga_final = t.factor_carga()
        tamaño_final = t.tamaño
    try:
        tiempo = timeit.timeit(test, number=reps)
        return tiempo, factor_carga_final, tamaño_final
    except Exception as e:
        print(f"[ERROR] {metodo_colision} | tamaño={tamaño} | n={n}: {e}")
        return None, None, None




def main():
    resultados = []
    print("BENCHMARK TABLAS HASH: Comparación de métodos de colisión y datasets")
    print("---------------------------------------------------------------")
    for metodo_colision in METODOS_COLISION:
        for tamaño_tabla in TAMANIOS_TABLA:
            for dataset_func, dataset_nombre in DATASETS:
                for n in CANTIDADES:
                    reps = REPS[n]
                    # Palabras comunes: tamaño fijo
                    if dataset_nombre == 'palabras_comunes':
                        claves_valores = dataset_func(n, tamaño_tabla)
                        if len(claves_valores) < n:
                            continue
                        claves, valores = zip(*claves_valores)
                    else:
                        claves_valores = dataset_func(n, tamaño_tabla)
                        claves, valores = zip(*claves_valores)
                    # Evitar pruebas inválidas para open addressing
                    if metodo_colision == 'open_addressing' and n > tamaño_tabla:
                        print(f"[SKIP] {metodo_colision} | tamaño={tamaño_tabla} | n={n}: demasiados elementos para open addressing")
                        resultados.append({
                            'metodo_colision': metodo_colision,
                            'tamaño_tabla': tamaño_tabla,
                            'elementos': n,
                            'dataset': dataset_nombre,
                            'repeticiones': reps,
                            'tiempo_total': None,
                            'tiempo_promedio': None,
                            'factor_carga_final': None,
                            'tamaño_final': None,
                            'nota': 'demasiados elementos para open addressing'
                        })
                        continue
                    t_tabla, factor_carga_final, tamaño_final = benchmark_tabla_busqueda(n, reps, claves, valores, metodo_colision, tamaño_tabla)
                    resultados.append({
                        'metodo_colision': metodo_colision,
                        'tamaño_tabla': tamaño_tabla,
                        'elementos': n,
                        'dataset': dataset_nombre,
                        'repeticiones': reps,
                        'tiempo_total': t_tabla,
                        'tiempo_promedio': t_tabla / reps if t_tabla is not None else None,
                        'factor_carga_final': factor_carga_final,
                        'tamaño_final': tamaño_final,
                        'nota': ''
                    })
                    print(f"{metodo_colision} | {dataset_nombre} | tamaño={tamaño_tabla} | n={n}: {t_tabla}")
    # Exportar a CSV
    fieldnames = ['metodo_colision','tamaño_tabla','elementos','dataset','repeticiones','tiempo_total','tiempo_promedio','factor_carga_final','tamaño_final','nota']
    with open('benchmark_iterable_resultados.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(resultados)
    print("\nResultados exportados a benchmark_iterable_resultados.csv")
    print("\nNOTA: Para open addressing, solo se ejecutan pruebas donde elementos <= tamaño_tabla. Si no, se marca como 'demasiados elementos para open addressing' en el CSV.")

if __name__ == "__main__":
    main()
