"""
Genera gráficos comparativos de los resultados del benchmark de tablas hash.
- Un gráfico por dataset y método de colisión.
- Eje X: cantidad de elementos
- Eje Y: tiempo promedio de búsqueda (s)
- Colores: tamaño de tabla
- Guarda los gráficos en benchmark_graficos/
"""
import pandas as pd
import matplotlib.pyplot as plt
import os

RESULTS_CSV = "benchmark_iterable_resultados.csv"
OUTDIR = "benchmark_graficos"

# Leer resultados
results = pd.read_csv(RESULTS_CSV)

# Filtrar solo filas válidas
results = results[results['tiempo_promedio'].notnull()]

# Listas únicas
datasets = results['dataset'].unique()
metodos = results['metodo_colision'].unique()
tamanios = sorted(results['tamaño_tabla'].unique())

# Graficar por dataset y método
for dataset in datasets:
    for metodo in metodos:
        df = results[(results['dataset'] == dataset) & (results['metodo_colision'] == metodo)]
        if df.empty:
            continue
        plt.figure(figsize=(8,6))
        for tam in tamanios:
            sub = df[df['tamaño_tabla'] == tam]
            if sub.empty:
                continue
            plt.plot(sub['elementos'], sub['tiempo_promedio'], marker='o', label=f"Tabla {tam}")
        plt.title(f"{metodo.title()} - Dataset: {dataset}")
        plt.xlabel("Cantidad de elementos")
        plt.ylabel("Tiempo promedio de búsqueda (s)")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        fname = f"{metodo}_{dataset}.png"
        plt.savefig(os.path.join(OUTDIR, fname))
        plt.close()

# Gráfico resumen: factor de carga final vs tiempo promedio
plt.figure(figsize=(8,6))
for metodo in metodos:
    sub = results[results['metodo_colision'] == metodo]
    plt.scatter(sub['factor_carga_final'], sub['tiempo_promedio'], alpha=0.6, label=metodo)
plt.title("Factor de carga final vs Tiempo promedio de búsqueda")
plt.xlabel("Factor de carga final")
plt.ylabel("Tiempo promedio de búsqueda (s)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "factor_carga_vs_tiempo.png"))
plt.close()

print(f"Gráficos generados en {OUTDIR}/")
