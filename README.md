# Data Analyst — Portfolio de aprendizaje

> ## ⚠️ Nota de autoría
> **Todo el código de este repositorio está escrito a mano por Miguel Ángel.** La IA (Claude)
> se usa **exclusivamente** para:
> 1. Plantear o proponer ejercicios,
> 2. Corregir o revisar el código **después** de haber sido escrito,
> 3. Generar esta documentación (READMEs, clasificación por tema, plantillas).
>
> **La IA nunca genera el código de los ejercicios en sí**, salvo dos excepciones puntuales,
> explícitamente marcadas como tales en `Agentes/agente_2/README.md` (no ocultas, no
> presentadas como propias). Esta declaración se repite en cada README temático y en cada
> entrada individual de ejercicio.

## Quién soy

Miguel Ángel Leo Acedo. Vengo de formación y experiencia en farmacia, y estoy haciendo la
transición hacia el análisis de datos — por eso casi todos los ejercicios de este repositorio
usan datos de farmacia, medicamentos, stock, ventas y alertas sanitarias: no es casualidad,
es el dominio que mejor conozco y donde primero quiero aportar valor con datos.

Mi objetivo es entrar en un puesto de **junior data analyst**, y a partir de ahí seguir
aprendiendo con la misma lógica con la que está construido este repositorio: sin atajos, sin
ocultar lo que todavía no domino, y siempre preguntándome para qué sirve realmente lo que
estoy construyendo.

## Qué hacemos aquí y por qué

Este repositorio no es una colección de ejercicios sueltos hechos por hacer. Cada carpeta
temática es una fase de aprendizaje deliberada, y `Agentes/` es un paso más allá: proyectos
que ya intentan resolver un problema real (analizar ventas de farmacia, cruzar alertas de la
FDA, interpretar resultados con un LLM), no solo practicar sintaxis.

La idea de fondo es simple: **no construyo herramientas por construirlas — construyo
herramientas que tengan sentido de utilidad**, aunque estén incompletas o tengan errores
todavía. Por eso los fallos y los ejercicios sin terminar se documentan en vez de esconderse
(ver `errores-recurrentes.md`): un portfolio honesto sobre lo que sé y lo que estoy
aprendiendo me parece más útil, tanto para quien lo revise como para mí mismo, que uno que
solo enseña resultados pulidos.

## Cómo pretendo seguir aprendiendo

- **Seguimiento activo de mis propios errores** (`errores-recurrentes.md`): cuando un patrón
  de error se repite, queda registrado y priorizado, no se repite en silencio.
- **De ejercicio suelto a herramienta con propósito**: la progresión de este repo va desde
  fundamentos de Python hasta `Agentes/`, proyectos que ya combinan APIs reales, pandas y un
  LLM para producir algo que un farmacéutico podría usar de verdad.
- **Revisión honesta, no autocomplaciente**: reviso y corrijo con ayuda de IA después de
  escribir el código, nunca antes — el objetivo es entender el fallo, no que desaparezca.

## Estructura

```
.
├── fundamentos-python/   # Listas, tuplas, dicts, sets, strings, bucles (sin librerías)
├── oop/                  # Clases, atributos privados, typing, logging/excepciones
├── numpy/                # Arrays, operaciones matriciales, PCA manual
├── pandas/               # DataFrames, limpieza de datos, groupby, series temporales
├── Agentes/              # Proyectos con API real + pandas + LLM (Gemini)
├── dataset/              # Datasets de ejemplo usados por los ejercicios
├── requirements.txt      # Dependencias del repositorio, comentadas en ES/EN
├── errores-recurrentes.md  # Seguimiento de patrones de error y huecos de conocimiento
```

Cada carpeta temática tiene su propio `README.md` con una entrada detallada por ejercicio
(fecha, concepto, dificultad, estado, qué practica, notas y autoría), en español e inglés.

## Resumen de ejercicios por tema

| Tema | Ejercicios | Rango de fechas | Estado general |
|---|---|---|---|
| [fundamentos-python](fundamentos-python/README.md) | 9 | 2026-07-31 → 2026-08-11 | 6 ✅ funcionales · 3 ⚠️ con errores/incompletos |
| [oop](oop/README.md) | 5 | 2026-08-06 → 2026-08-11 | 4 ⚠️ con errores/incompletos · 1 🔄 en progreso |
| [numpy](numpy/README.md) | 2 | 2026-08-13 → 2026-08-21 | 1 ✅ funcional · 1 ⚠️ con errores |
| [pandas](pandas/README.md) | 4 | 2026-08-25 → 2026-08-29 | 2 ✅ funcionales · 2 ⚠️ con errores |
| [Agentes](Agentes/agente_2/README.md) | 2 | 2026-08 → 2026-09 | `agente_2` ✅ ejecuta de principio a fin (API FDA + pandas + Gemini); `agente_1.1` recuperado de un proyecto anterior, sirve de referencia de diseño |

**Total: 22 ejercicios/proyectos.**

## Cómo ejecutar

```
pip install -r requirements.txt
```

Los proyectos de `Agentes/` necesitan además su propio `.env` (no incluido, cada carpeta
tiene su `.gitignore`) con una clave de API de Gemini — ver el README de cada agente.

## Nota sobre las fechas

Las fechas usadas en la reorganización de los ejercicios por tema corresponden a la **fecha
de modificación del archivo** (más granular que el historial de git, que en este repo agrupa
varios archivos en los mismos commits). A partir de esa reorganización, el historial de git es
la fuente de verdad para los ejercicios nuevos.

---

# Data Analyst — Learning Portfolio (EN)

> ## ⚠️ Authorship note
> **All code in this repository is hand-written by Miguel Ángel.** AI (Claude) is used
> **exclusively** to: propose exercises, review/correct code **after** it was written, and
> generate this documentation. **AI never writes the exercises' code itself**, with two
> explicit, clearly marked exceptions documented in `Agentes/agente_2/README.md`.

## Who I am

Miguel Ángel Leo Acedo. I come from a pharmacy background and am transitioning into data
analysis — that's why most exercises here use pharmacy, drug stock, sales, and health-alert
data: it's the domain I know best and where I want to bring value with data first. My goal is
a **junior data analyst** role, and to keep learning the same way this repository is built:
no shortcuts, nothing hidden, always asking what a tool is actually useful for.

## What we do here and why

This isn't a pile of exercises done for their own sake. Each topic folder is a deliberate
learning phase, and `Agentes/` goes further: projects that already attempt to solve a real
problem (analyzing pharmacy sales, cross-referencing FDA recalls, interpreting results with an
LLM), not just practicing syntax. **I don't build tools just to build them — I build tools
meant to be genuinely useful**, even while incomplete. Failures and unfinished exercises are
documented, not hidden (see `errores-recurrentes.md`) — an honest portfolio about what I know
and what I'm still learning is more useful, to a reviewer and to myself, than one that only
shows polished results.

## How I plan to keep learning

- **Active tracking of my own errors** (`errores-recurrentes.md`): recurring patterns get
  logged and prioritized, not silently repeated.
- **From loose exercise to purposeful tool**: this repo's progression runs from Python
  fundamentals to `Agentes/`, projects that already combine real APIs, pandas, and an LLM to
  produce something a pharmacist could actually use.
- **Honest review, not self-flattering**: I review and correct with AI help after writing the
  code, never before — the goal is understanding the failure, not making it disappear.

See each topic folder's `README.md` for the full per-exercise breakdown in both Spanish and
English.
