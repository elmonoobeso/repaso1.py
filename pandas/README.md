# Pandas

> **Autoría:** Todo el código de esta carpeta está escrito a mano por el usuario. La IA se usa
> exclusivamente para plantear/proponer ejercicios, corregir o revisar el código después de
> haber sido escrito, y para generar esta documentación. La IA nunca genera el código de los
> ejercicios en sí.

Estos son **ejercicios de estudio** de pandas: tipado, filtros, limpieza de datos (nulos,
duplicados, outliers), agregaciones (`groupby`), combinación de tablas y series temporales,
sobre un dataset de ejemplo de una farmacia. El nivel de dificultad de cada ejercicio se
indica en su entrada correspondiente.

---

## 2026-08-25 — Exploración de tipos, filtros y `loc`
**Concepto:** `dtypes`, `astype`, `pd.to_datetime`, filtros booleanos, `loc`, `describe`
**Dificultad:** Básico
**Estado:** ✅ Funcional
**Qué practica:** Corregir el tipo de una columna numérica leída como `object`, convertir
fechas, filtrar por stock bajo y por categoría, y seleccionar columnas con `loc`.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-25_exploracion-tipos-filtros-loc.py](2026-08-25_exploracion-tipos-filtros-loc.py)

## 2026-08-26 — Duplicados, nulos y outliers (IQR)
**Concepto:** `duplicated`, `isnull`, `fillna`, detección de outliers con rango intercuartílico
(IQR), renombrado de columnas, histograma con matplotlib
**Dificultad:** Intermedio
**Estado:** ⚠️ Con errores conocidos
**Qué practica:** Detectar y revisar filas duplicadas y valores nulos, rellenar un nulo
puntual con `.loc`, calcular límites de outliers con IQR (en vez de z-score, por no asumir
distribución normal en precios), y visualizar la distribución de precios.
**Notas/aprendizajes:** `df.drop_duplicates()` y `df["stock"].fillna(df["stock"].median())`
se llaman sin reasignar el resultado (`df = df.drop_duplicates()` / `df["stock"] = ...`) —
pandas no modifica en el sitio por defecto, así que los nulos/duplicados siguen apareciendo
después. El propio autor documenta la confusión en el comentario ("porque no me ha
funcionado??", "porque no sale el valor corregido???"), quedando como aprendizaje explícito
sobre mutabilidad en pandas.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-26_duplicados-nulos-outliers-iqr.py](2026-08-26_duplicados-nulos-outliers-iqr.py)

## 2026-08-28 — `groupby`, `transform`, `merge` y `pivot`
**Concepto:** Agregación por grupo (`groupby().sum()`), medias por grupo sin colapsar filas
(`transform`), binning (`pd.cut`), combinación de tablas (`merge`), tablas dinámicas (`pivot`)
**Dificultad:** Intermedio-Avanzado
**Estado:** ✅ Funcional
**Qué practica:** Calcular ingresos por producto, agregarlos por categoría, categorizar
precios en rangos, cruzar con una tabla de proveedores (`left join`) y construir una tabla
dinámica de ingresos por categoría y mes.
**Notas/aprendizajes:** El autor anota correctamente que los `NaN` en el `pivot` son
esperables (no todas las categorías tienen ingresos en todos los meses), no un error.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-28_groupby-transform-merge-pivot.py](2026-08-28_groupby-transform-merge-pivot.py)

## 2026-08-29 — Series temporales, `rolling` y `groupby`
**Concepto:** `pd.date_range`, medias móviles (`rolling`), `np.where` para clasificar,
`groupby().transform()` para comparar cada fila con la media de su grupo
**Dificultad:** Avanzado
**Estado:** ⚠️ Con errores conocidos
**Qué practica:** Generar un dataset sintético de ventas con `numpy.random`, clasificar
ingresos como "caro"/"barato", calcular una media móvil de 5 días, y marcar qué filas están
por encima de la media de ingresos de su propio producto.
**Notas/aprendizajes:** La función `es_ventas_fuerte` contiene un error de sintaxis grave:
`int(i)=datos["unidades_vendidas"]` intenta asignar un valor al resultado de una llamada a
función, lo cual es un `SyntaxError` en Python (no una asignación válida). Además la
comprensión de conjuntos dentro de la función referencia `unidades_vendidas` sin que exista
en ese ámbito. Al ser un `SyntaxError`, el archivo completo no se puede ejecutar tal cual
está — se conserva sin corregir para reflejar el punto exacto del aprendizaje.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-29_series-temporales-rolling-groupby.py](2026-08-29_series-temporales-rolling-groupby.py)

---

# Pandas (EN)

> **Authorship:** All code in this folder is hand-written by the user. AI is used exclusively
> to propose/suggest exercises, review or correct code after it was written, and to generate
> this documentation. AI never writes the exercises' code itself.

These are **study exercises** covering pandas typing, filtering, data cleaning (nulls,
duplicates, outliers), aggregation (`groupby`), table merging, and time series, over a sample
pharmacy dataset. Each entry above states its difficulty level; see the Spanish section for
full per-exercise detail (same structure — Date/Concept/Difficulty/Status/What it
practices/Notes/Authorship/Code).
