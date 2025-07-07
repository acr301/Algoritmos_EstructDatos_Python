
# Bitácora de Desarrollo

## Cambios recientes

- Se modularizó la resolución de colisiones:
  - Ahora los métodos de direccionamiento abierto (lineal, cuadrático, double hashing, random) están en `resolucion_colisiones_direccionamiento.py`.
  - El encadenamiento (chaining) usa `defaultdict` y está en `resolucion_colisiones_encadenamiento.py`.
- Se aprovecha `defaultdict` para simplificar la gestión de cubetas en chaining.
- La clase principal (`TablaHashIterable`) ahora es más limpia y delega la lógica de colisiones a estos módulos.
- Se agregaron más tipos de sondeos para open addressing, facilitando la comparación experimental.

## Próximos pasos

1. **Tamaño de la tabla y función hash**
   - Permitir que el tamaño de la tabla sea primo o potencia de 2 según el método de hash/sondeo.
   - Documentar cómo el tamaño afecta la dispersión y la eficiencia.

2. **Factor de carga y redimensionamiento**
   - Medir el factor de carga (`elementos / tamaño`).
   - Implementar redimensionamiento automático cuando se supere un umbral (ej: 0.7).
   - Al redimensionar:
     - Si el hash es modular, buscar el siguiente primo.
     - Si es por potencias de 2, duplicar tamaño.
   - Re-hashear todos los elementos al redimensionar.

3. **Dataset original y benchmarking reproducible**
   - Permitir usar un dataset predefinido para pruebas consistentes.
   - Si no se pasa dataset, generar datos aleatorios.
   - Registrar el factor de carga y el tamaño de la tabla en los resultados del benchmark.


## Implementación del nuevo benchmark y visualización

- El benchmark fue refactorizado para:
  - Eliminar dependencias innecesarias y centrarse en los métodos de colisión y datasets relevantes.
  - Registrar en el CSV: método de colisión, tamaño de tabla, cantidad de elementos, dataset, repeticiones, tiempo total/promedio, factor de carga final, tamaño final y notas.
  - Facilitar el análisis y la visualización didáctica de los resultados.

- Se creó el script `benchmark_graficos/graficar_benchmark.py` que genera automáticamente los siguientes gráficos:

### Figura 1. Comparación de métodos de colisión por dataset
Para cada combinación de método de colisión (`chaining`, `open_addressing`) y dataset (`aleatorio`, `secuencial`, `colisiones`, `palabras_comunes`):
- **Eje X:** cantidad de elementos
- **Eje Y:** tiempo promedio de búsqueda (s)
- **Colores:** tamaño de tabla
- **Interpretación:** Permite observar cómo escala el tiempo de búsqueda según el método y el tipo de datos. Se visualiza el impacto de la carga y la dispersión de la función hash.

### Figura 2. Factor de carga final vs. tiempo promedio
- **Eje X:** factor de carga final (elementos / tamaño de tabla)
- **Eje Y:** tiempo promedio de búsqueda (s)
- **Colores:** método de colisión
- **Interpretación:** Muestra la sensibilidad de cada método al aumento de la carga. Se observa cómo el rendimiento se degrada al acercarse al límite de la tabla, especialmente en open addressing.

---

**Conclusiones de los gráficos:**
- El método de colisión y el tipo de datos afectan significativamente el rendimiento.
- El chaining es más robusto ante cargas altas y colisiones, pero puede crecer en memoria.
- Open addressing es eficiente con baja carga, pero sufre mucho cuando la tabla se llena.
- El factor de carga es clave para dimensionar la tabla y evitar degradación.

**Recomendación:**
Usar ambos gráficos para presentar y discutir resultados en la exposición, destacando patrones y anomalías según el dataset y el método de colisión.

---

**Esta bitácora documenta las decisiones, resultados y visualizaciones clave para mantener trazabilidad y facilitar la colaboración.**
