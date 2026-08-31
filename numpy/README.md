# NumPy

> **Autoría:** Todo el código de esta carpeta está escrito a mano por el usuario. La IA se usa
> exclusivamente para plantear/proponer ejercicios, corregir o revisar el código después de
> haber sido escrito, y para generar esta documentación. La IA nunca genera el código de los
> ejercicios en sí.

Estos son **ejercicios de estudio** de NumPy: creación de arrays, operaciones matriciales y
un caso completo de PCA manual. El nivel de dificultad de cada ejercicio se indica en su
entrada correspondiente.

---

## 2026-08-13 — Arrays básicos de NumPy
**Concepto:** Creación de arrays (`np.array`, `np.ones`, `np.full_like`, `np.random.randint`),
atributos de forma (`ndim`, `shape`, `itemsize`), slicing e indexado
**Dificultad:** Básico
**Estado:** ⚠️ Con errores conocidos
**Qué practica:** Leer una fila de un CSV con el módulo `csv`, convertirla en array de NumPy
y explorar sus atributos y operaciones básicas de copia/slicing.
**Notas/aprendizajes:** Varios errores de API: `limpio.range()` no existe en NumPy (no hay
método `.range()` en un array); `limpio.shape()` se llama como método cuando `shape` es un
**atributo**, no una función (debería ser `limpio.shape` sin paréntesis); `np.itemsize(limpio)`
tampoco existe como función standalone (`itemsize` es un atributo del array); y
`np.random.randint(0,8,0,8)` repite los límites en la posición de `size`, una firma incorrecta.
El archivo no llegaría a ejecutarse completo tal como está. Documentado como aprendizaje, sin
corregir.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-13_arrays-basicos-con-errores.py](2026-08-13_arrays-basicos-con-errores.py)

## 2026-08-21 — PCA manual con autovalores/autovectores
**Concepto:** Matriz de covarianza (`np.cov`), descomposición espectral (`np.linalg.eig`),
varianza explicada acumulada (`np.cumsum`), reducción de dimensionalidad, máscaras booleanas
con `np.isnan`
**Dificultad:** Avanzado
**Estado:** ✅ Funcional
**Qué practica:** Implementar PCA "a mano" (sin `sklearn`): calcular la matriz de covarianza,
obtener autovalores/autovectores, ordenarlos por varianza explicada, quedarse con los 6
componentes principales que explican más del 95% de la varianza, y proyectar el dataset
reducido. Incluye además slicing 2D, `np.vstack`/`np.hstack` para añadir filas/columnas de
máximos, y una combinación de máscaras (`~fraccion_nan & condicion1`).
**Notas/aprendizajes:** Buen manejo de la parte real de los autovalores/autovectores
(`.real`) para evitar artefactos numéricos complejos. El bloque final de máscaras NaN queda
como exploración sin imprimir/usar el resultado.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-21_pca-manual-autovalores.py](2026-08-21_pca-manual-autovalores.py)

---

# NumPy (EN)

> **Authorship:** All code in this folder is hand-written by the user. AI is used exclusively
> to propose/suggest exercises, review or correct code after it was written, and to generate
> this documentation. AI never writes the exercises' code itself.

These are **study exercises** covering NumPy array creation, matrix operations, and a full
manual PCA implementation. Each entry above states its difficulty level; see the Spanish
section for full per-exercise detail (same structure — Date/Concept/Difficulty/Status/What it
practices/Notes/Authorship/Code).
