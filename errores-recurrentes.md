# Errores recurrentes y huecos de conocimiento
Último análisis: 2026-08-31 (hasta commit 043e028)

Cuando pases esta lista para pedir ejercicios de repaso, ya viene
agrupada por prioridad — no hace falta que añadas nada.

## 🔴 Prioridad alta

- **Manejo de excepciones** — decisión subóptima: `except` demasiado amplio o sin tipar,
  usado de forma inconsistente. En `fundamentos-python/2026-08-04_normalizacion-segmentacion-sets.py`
  (`segmentacion`) hay un `except:` desnudo que traga cualquier error sin información. En
  `oop/2026-08-11_clase-csvanalyzer-parseo.py` (`parseo`) se usa `except Exception as error`
  genérico sin diferenciar tipos. Contrasta con `oop/2026-08-07_clase-datapipeline-logging-excepciones.py`,
  donde sí se hace bien (excepciones específicas `ZeroDivisionError`/`TypeError` antes del
  `Exception` genérico) — el patrón correcto ya se domina, pero no se aplica de forma constante.
  Visto en: fundamentos-python/2026-08-04, oop/2026-08-11 (2026-08-11).

- **Pandas — olvidar reasignar operaciones que no mutan in-place** — decisión subóptima
  recurrente en dos archivos distintos: `df.drop_duplicates()` y
  `df["stock"].fillna(df["stock"].median())` se llaman sin reasignar en
  `pandas/2026-08-26_duplicados-nulos-outliers-iqr.py` (el propio autor documenta la confusión
  en el comentario: "porque no sale el valor corregido???"); `df.set_index("fecha")` y
  `df.sort_index()` tienen el mismo problema en `pandas/2026-08-29_series-temporales-rolling-groupby.py`.
  Es el mismo hueco conceptual repitiéndose 3 días después sin haberse consolidado.
  Visto en: pandas/2026-08-26, pandas/2026-08-29.

- **Pandas — groupby mal indexado/alineado** — decisión subóptima: en
  `pandas/2026-08-29_series-temporales-rolling-groupby.py`, la línea
  `df["ingresos_medio_producto"]=df.groupby("producto")["ingresos"].mean()` asigna
  directamente el resultado de un `groupby().mean()` (indexado por `producto`, con menos
  filas que `df`) a una columna del DataFrame original — esto no alinea correctamente y
  genera `NaN`/valores mal emparejados. La línea inmediatamente siguiente usa
  `.transform("mean")`, que sí es la forma correcta, así que el propio archivo contiene el
  contraste entre el patrón malo y el bueno sin que quede señalado como tal.
  Visto en: pandas/2026-08-29.

- **Validación de tipos con `typing`** — errores de sintaxis/ejecución: en
  `oop/2026-08-10_clases-filtrado-truthiness.py`, `ECommerceAnalyzer` usa
  `Dict[str,Dict[str,anyy]]` (typo `anyy` en vez de `Any`) → `NameError` al definir la clase;
  `PharmacyBatchAnalyzer` usa `Tuple(List[dict[str,any]])` con paréntesis en vez de corchetes,
  sintaxis inválida para genéricos de `typing` → error al evaluar la anotación. Dos fallos de
  sintaxis distintos sobre el mismo concepto en el mismo archivo — indica que el hint de tipos
  compuestos (`Dict`/`Tuple` anidados) todavía no está consolidado, más allá del typo puntual.
  Visto en: oop/2026-08-10.

- **`SyntaxError` bloqueante en pandas** — error de sintaxis/ejecución: en
  `pandas/2026-08-29_series-temporales-rolling-groupby.py`, la función `es_ventas_fuerte`
  contiene `int(i)=datos["unidades_vendidas"]`, una asignación a una llamada de función, que
  es un `SyntaxError` de Python — impide que el **archivo completo** se ejecute, no solo esa
  función. Es el error más severo del repo. La función también referencia
  `unidades_vendidas` sin que exista en su ámbito (debería ser `datos["unidades_vendidas"]`
  o el parámetro `i`).
  Visto en: pandas/2026-08-29.

- **Hueco: manejo de APIs/requests** — no aparece ni una sola vez en todo el repo: no hay
  `import requests`, ni llamadas HTTP, ni manejo de respuestas/errores de red. Es un concepto
  de la lista de alto valor totalmente ausente.
  Visto en: (ningún archivo — ausencia total).

- **Hueco: estructuras de control en flujos de agentes** — la carpeta
  `agentes-automatizacion/` no tiene contenido; no hay ningún ejercicio de orquestación,
  máquina de estados, reintentos, ni lógica de control pensada para un flujo de agente.
  Visto en: (ningún archivo — ausencia total).

## 🟡 Prioridad media

- **Estructuras de control — bug de variable en condición** — decisión subóptima: en
  `fundamentos-python/2026-08-04_normalizacion-segmentacion-sets.py`, `pipeline_control`
  compara `id` (la lista completa recibida como parámetro) contra `5`/`15` en vez de `i` (el
  elemento actual del bucle) — el `continue`/`break` nunca se dispara como se pretende.
  Visto en: fundamentos-python/2026-08-04.

- **Ejercicios sin terminar sobre validación por truthiness** — hueco/decisión pendiente:
  `procesar_registro` queda como stub (`pass`) tanto en
  `fundamentos-python/2026-08-05_while-defaults-fromkeys.py` como en
  `oop/2026-08-06_args-logging-clase-inventario.py` — el mismo patrón de ejercicio (filtrar
  con truthiness y acumular en una lista) queda incompleto dos veces en días distintos.
  Visto en: fundamentos-python/2026-08-05, oop/2026-08-06.

- **Type hint inválido como expresión booleana** — decisión subóptima: en
  `fundamentos-python/2026-08-05_while-defaults-fromkeys.py`,
  `def logs(*metricas:dict!=None,idd:list=None):` usa `dict!=None` (una comparación que
  evalúa a `True`) como anotación de tipo, en vez de `Optional[dict]` o similar. No rompe en
  runtime porque Python no valida anotaciones por defecto, pero revela que el propósito de
  los type hints (documentar/validar tipo esperado, no expresar una condición) no está claro
  todavía.
  Visto en: fundamentos-python/2026-08-05.

- **OOP — método privado sin exponer públicamente** — decisión subóptima: en
  `oop/2026-08-07_clase-datapipeline-logging-excepciones.py`, `DataPipeline.__calcular_duracion`
  es un método privado (name-mangled) pero la clase no tiene ningún método público que lo
  invoque — el cálculo de duración nunca se expone ni se ejecuta/testea.
  Visto en: oop/2026-08-07.

- **OOP — método que no retorna resultado útil** — decisión subóptima: en
  `oop/2026-08-11_clase-csvanalyzer-parseo.py`, `get_valid_stocks` filtra líneas válidas en
  `validos` pero termina con `return` vacío — el trabajo del método se pierde, no hay forma
  de usar el resultado desde fuera.
  Visto en: oop/2026-08-11.

- **`NameError` básico + archivo incompleto** — error de sintaxis/ejecución: en
  `oop/2026-08-11_clase-jsonapianalyzer-incompleta.py`, `ruta=dataset/"doc_prueba.json"` usa
  la variable `dataset` sin definir (debía ser `prueba_json`), y hay dos llamadas
  `open(self.__file_path,)` con coma colgante sin argumento — el archivo no llega a
  ejecutarse en ningún punto.
  Visto en: oop/2026-08-11.

## 🟢 Prioridad baja / repaso opcional

- **NumPy — atributos usados como métodos / funciones inexistentes** — errores de
  sintaxis/ejecución: `limpio.range()` no existe en un array de NumPy; `limpio.shape()` se
  llama como método cuando `shape` es un atributo (`limpio.shape`, sin paréntesis);
  `np.itemsize(limpio)` no existe como función standalone (`itemsize` es atributo del array);
  `np.random.randint(0,8,0,8)` repite los límites en la posición de `size`. NumPy no está en
  la lista de alto valor explícita, pero es la base de pandas.
  Visto en: numpy/2026-08-13.

- **Redundancia / código duplicado** — decisión subóptima menor: en
  `fundamentos-python/2026-08-03_eliminar-duplicados-orden.py`, se deduplica primero con un
  bucle manual y después se aplica `dict.fromkeys()` sobre el resultado ya limpio (doble
  trabajo). En `oop/2026-08-06_args-logging-clase-inventario.py`, `Inventario.obtener_resumen`
  y `obtener_resumen2` hacen exactamente lo mismo (comprensión vs. bucle explícito) sin que
  quede claro cuál es la versión "final".
  Visto en: fundamentos-python/2026-08-03, oop/2026-08-06.

- **Ventana deslizante O(n·k)** — decisión subóptima menor: en
  `fundamentos-python/2026-08-03_ventana-deslizante-maximos.py`, el máximo por ventana se
  recalcula con slicing en cada posición; una estructura tipo deque monotónico lo resolvería
  en O(n). No es un error, es una optimización futura.
  Visto en: fundamentos-python/2026-08-03.

- **Ejercicio sin terminar sobre tuplas/listas anidadas** — `congelar_registro` en
  `fundamentos-python/2026-08-03_tuplas-con-listas-mutables.py` no hace nada observable
  (no imprime ni retorna). Bajo impacto porque el concepto (mutabilidad anidada) no está en
  la lista de alto valor.
  Visto en: fundamentos-python/2026-08-03.

## ✅ Superados

*(vacío — primer análisis del repo, aún no hay progreso que comparar entre ejecuciones)*
