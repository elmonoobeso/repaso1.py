# Fundamentos de Python

> **Autoría:** Todo el código de esta carpeta está escrito a mano por el usuario. La IA se usa
> exclusivamente para plantear/proponer ejercicios, corregir o revisar el código después de
> haber sido escrito, y para generar esta documentación. La IA nunca genera el código de los
> ejercicios en sí.

Estos son **ejercicios de estudio** de repaso de Python básico e intermedio: manejo de listas,
tuplas, diccionarios, sets, strings, bucles y estructuras de control, sin librerías externas.
El nivel de dificultad de cada ejercicio se indica en su entrada correspondiente.

---

## 2026-07-31 — Invertir palabras largas
**Concepto:** Slicing de strings y `str.split()` / `str.join()`
**Dificultad:** Básico
**Estado:** ✅ Funcional
**Qué practica:** Recorrer las palabras de una frase e invertir (con `[::-1]`) solo las que
superan una longitud determinada, reconstruyendo la frase con `join`.
**Notas/aprendizajes:** Primer uso consciente de `join` para pasar de lista a texto.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-07-31_invertir-palabras-largas.py](2026-07-31_invertir-palabras-largas.py)

## 2026-08-03 — Eliminar duplicados manteniendo el orden
**Concepto:** `dict.fromkeys()` como truco de deduplicación estable
**Dificultad:** Básico
**Estado:** ✅ Funcional
**Qué practica:** Eliminar duplicados de una lista conservando el orden de primera aparición.
**Notas/aprendizajes:** La función construye la lista limpia "a mano" con un bucle y luego,
de forma algo redundante, aplica también `dict.fromkeys()` sobre el resultado ya limpio.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-03_eliminar-duplicados-orden.py](2026-08-03_eliminar-duplicados-orden.py)

## 2026-08-03 — Tuplas inmutables con listas mutables dentro
**Concepto:** Mutabilidad anidada (`tuple` que contiene una `list`) e `isinstance`
**Dificultad:** Básico
**Estado:** ⚠️ Con errores conocidos
**Qué practica:** Modificar el elemento lista de una tupla sin necesidad de reconstruir toda
la tupla, y diferenciar `type() ==` de `isinstance()`.
**Notas/aprendizajes:** `congelar_registro` queda sin terminar (no imprime ni retorna nada);
queda como ejercicio pendiente de completar.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-03_tuplas-con-listas-mutables.py](2026-08-03_tuplas-con-listas-mutables.py)

## 2026-08-03 — Validación de acceso con lógica booleana
**Concepto:** Combinación de operadores `and`/`or`/`not` en una condición compuesta
**Dificultad:** Básico
**Estado:** ✅ Funcional
**Qué practica:** Construir una regla de autorización (usuario activo, no bloqueado, admin u
owner del recurso no privado) en una sola expresión booleana.
**Notas/aprendizajes:** Autocrítica correcta en comentario: comparar `== True` / `== False`
es redundante, basta con el valor o su negación.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-03_validacion-acceso-booleana.py](2026-08-03_validacion-acceso-booleana.py)

## 2026-08-03 — Ventana deslizante de máximos
**Concepto:** Sliding window con slicing de listas y `max()`
**Dificultad:** Básico-Intermedio
**Estado:** ✅ Funcional
**Qué practica:** Calcular el máximo de cada subventana de tamaño `k` sobre una lista.
**Notas/aprendizajes:** Solución O(n·k) por slicing; posible mejora futura con una
estructura tipo deque para O(n).
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-03_ventana-deslizante-maximos.py](2026-08-03_ventana-deslizante-maximos.py)

## 2026-08-04 — Normalización de strings, segmentación y sets
**Concepto:** `str.strip()/capitalize()`, filtrado con `try/except`, `set.union()/difference()`
**Dificultad:** Básico
**Estado:** ⚠️ Con errores conocidos
**Qué practica:** Cinco mini-ejercicios: normalizar texto, segmentar transacciones por umbral,
operar con sets, comprobar claves en diccionarios y control de flujo con `continue`/`break`.
**Notas/aprendizajes:** `pipeline_control` (ejercicio 5) compara `id` (la lista completa)
contra `5`/`15` en vez de `i` (el elemento actual dentro del bucle) — el `continue`/`break`
nunca se dispara como se pretende. Queda documentado como aprendizaje, no corregido.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-04_normalizacion-segmentacion-sets.py](2026-08-04_normalizacion-segmentacion-sets.py)

## 2026-08-05 — Strings, sets y limpieza con `while`
**Concepto:** `str.strip()/capitalize()`, `set.difference()`, depuración con `while`
**Dificultad:** Básico-Intermedio
**Estado:** ✅ Funcional
**Qué practica:** Limpiar un log de alerta, filtrar tickers restringidos de una cartera con
sets, y eliminar ceros de una lista de precios con un bucle `while`.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-05_strings-sets-while.py](2026-08-05_strings-sets-while.py)

## 2026-08-05 — `while`, valores por defecto y `dict.fromkeys`
**Concepto:** Mutación de lista en un bucle `while` durante la iteración, parámetros opcionales,
`dict.fromkeys()`
**Dificultad:** Intermedio
**Estado:** ⚠️ Con errores conocidos
**Qué practica:** Eliminar ceros de una lista con `while ... in`, validar argumentos por
defecto, e inicializar un diccionario de sensores con `dict.fromkeys`.
**Notas/aprendizajes:** `procesar_registro` queda sin implementar (`pass`). La firma
`def logs(*metricas:dict!=None, ...)` usa una expresión booleana (`dict!=None`) como type
hint, lo cual no es una anotación de tipo válida (Python no la evalúa en runtime, pero es
semánticamente incorrecta). El autor documenta honestamente que no logró añadir el mismo
valor a todas las claves de `dict.fromkeys` en la misma línea.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-05_while-defaults-fromkeys.py](2026-08-05_while-defaults-fromkeys.py)

## 2026-08-11 — Creación de JSON desde una lista de diccionarios
**Concepto:** `pathlib.Path`, mapeo de columnas a filas con `zip`, `json.dump`
**Dificultad:** Básico
**Estado:** ✅ Funcional
**Qué practica:** Convertir una tabla en formato "columnas + filas" en una lista de objetos
JSON usando `dict(zip(columnas, fila))`, y escribirla a disco con `pathlib`.
**Autoría:** Escrito a mano sin asistencia de IA. IA usada únicamente para corrección/revisión
posterior y para generar esta documentación.
**Código:** [2026-08-11_creacion-json-desde-lista.py](2026-08-11_creacion-json-desde-lista.py)

---

# Python Fundamentals (EN)

> **Authorship:** All code in this folder is hand-written by the user. AI is used exclusively
> to propose/suggest exercises, review or correct code after it was written, and to generate
> this documentation. AI never writes the exercises' code itself.

These are **study exercises** reviewing basic/intermediate Python: lists, tuples,
dictionaries, sets, strings, loops and control flow, without external libraries. Each entry
above states its difficulty level; see the Spanish section for the full per-exercise detail
(same structure — Fecha/Concepto/Dificultad/Estado/Qué practica/Notas/Autoría/Código).
