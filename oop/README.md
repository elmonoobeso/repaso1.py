# OOP (Programación Orientada a Objetos)

> **Autoría:** Todo el código de esta carpeta está escrito a mano por el usuario. La IA se usa
> exclusivamente para plantear/proponer ejercicios, corregir o revisar el código después de
> haber sido escrito, y para generar esta documentación. La IA nunca genera el código de los
> ejercicios en sí.

Estos son **ejercicios de estudio** centrados en clases, atributos "privados" (`__attr`),
type hints (`typing`) y su combinación con manejo de errores/logging. El nivel de dificultad
de cada ejercicio se indica en su entrada correspondiente.

---

## 2026-08-06 — `*args`, logging y clase `Inventario`
**Concepto:** Desempaquetado de argumentos variádicos, `dict.get()`, e introducción a clases
**Dificultad:** Intermedio
**Estado:** ⚠️ Con errores conocidos
**Qué practica:** Filtrar precios, procesar lotes de métricas con `*args`, y una primera
clase `Inventario` con métodos que devuelven listas en mayúsculas (dos formas: comprensión
y bucle explícito).
**Notas/aprendizajes:** `procesar_registro` es un stub sin implementar (`pass`), dejado
como plantilla del reto. El resto del archivo sí es funcional.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-06_args-logging-clase-inventario.py](2026-08-06_args-logging-clase-inventario.py)

## 2026-08-07 — Clase `DataPipeline`, logging y manejo de excepciones
**Concepto:** Atributos privados con `__init__`, `datetime`/`timedelta`, `logging`,
`try/except` con múltiples tipos de excepción
**Dificultad:** Intermedio-Avanzado
**Estado:** ⚠️ Con errores conocidos (versión corregida incluida en el mismo archivo)
**Qué practica:** Cinco ejercicios: filtrado de listas, acceso anidado a diccionarios, una
clase `DataPipeline` que calcula duración entre fechas, `*args` con parámetros nombrados, y
logging de errores en un pipeline con `try/except`.
**Notas/aprendizajes:** La primera versión de `ejercicio5` tiene una comprensión de lista
inválida (`for grupo.values() in grupo`) y usa una variable `i` no definida — no funciona
como se pretende. El propio archivo contiene, más abajo, una **versión corregida** con
excepciones específicas (`ZeroDivisionError`, `TypeError`) antes del genérico `Exception`.
Ambas versiones se conservan tal cual para mostrar el proceso de aprendizaje.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-07_clase-datapipeline-logging-excepciones.py](2026-08-07_clase-datapipeline-logging-excepciones.py)

## 2026-08-10 — Clases con filtrado por truthiness
**Concepto:** Atributos privados, `typing`, comprensiones de listas anidadas, evaluación
implícita (truthiness) para filtrar `0`/`None`/`""`
**Dificultad:** Intermedio-Avanzado
**Estado:** ⚠️ Con errores conocidos
**Qué practica:** Cinco clases (`SensorProcessor`, `ECommerceAnalyzer`,
`PharmacyBatchAnalyzer`, `StoreAnalyzer`, `SecurePipeline`) que limpian datos de sensores,
campañas de e-commerce, lotes de farmacia y transacciones de tiendas sin comparaciones
explícitas (`!= 0`, `is not None`).
**Notas/aprendizajes:** `ECommerceAnalyzer` referencia `anyy` (typo de `Any`) en su type
hint, lo que provoca `NameError` al instanciarse. `PharmacyBatchAnalyzer` usa
`Tuple(List[dict[str,any]])` con paréntesis en vez de corchetes, sintaxis inválida para
generics de `typing`. Documentado como aprendizaje sin corregir.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-10_clases-filtrado-truthiness.py](2026-08-10_clases-filtrado-truthiness.py)

## 2026-08-11 — Clase `CSVAnalyzer` y parseo de CSV
**Concepto:** Lectura de CSV con el módulo `csv`, `pathlib`, manejo de errores en el parseo
**Dificultad:** Intermedio
**Estado:** ⚠️ Con errores conocidos
**Qué practica:** Una clase que lee un inventario en CSV y calcula el total (`stock × precio`)
por producto, capturando errores de conversión de tipo por fila.
**Notas/aprendizajes:** `get_valid_stocks` filtra líneas válidas pero termina con un `return`
vacío — no retorna ni imprime el resultado, por lo que el método no tiene efecto observable.
`parseo()` sí funciona y es la versión utilizada en la ejecución final.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-11_clase-csvanalyzer-parseo.py](2026-08-11_clase-csvanalyzer-parseo.py)

## 2026-08-11 — Clase `JSONAPIAnalyzer` (incompleta)
**Concepto:** Lectura de JSON con `pathlib` y clases
**Dificultad:** Intermedio
**Estado:** 🔄 En progreso
**Qué practica:** Boceto inicial de una clase para leer y verificar montos desde un JSON.
**Notas/aprendizajes:** El archivo no llega a ejecutarse: la variable `dataset` se usa en
`ruta=dataset/"doc_prueba.json"` sin haber sido definida (debía ser `prueba_json`), y hay dos
llamadas `open(...)` con una coma colgante sin argumento ni bloque `with` cerrado
correctamente. Se conserva como estaba — es el ejercicio inacabado más reciente del repo.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-11_clase-jsonapianalyzer-incompleta.py](2026-08-11_clase-jsonapianalyzer-incompleta.py)

---

# OOP (Object-Oriented Programming) (EN)

> **Authorship:** All code in this folder is hand-written by the user. AI is used exclusively
> to propose/suggest exercises, review or correct code after it was written, and to generate
> this documentation. AI never writes the exercises' code itself.

These are **study exercises** focused on classes, "private" attributes (`__attr`), type
hints (`typing`), and combining them with error handling/logging. Each entry above states its
difficulty level; see the Spanish section for full per-exercise detail (same structure —
Date/Concept/Difficulty/Status/What it practices/Notes/Authorship/Code).
