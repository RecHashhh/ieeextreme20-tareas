# IEEEXtreme 20.0 · Banco de tareas

Recopilación de los 20 enunciados de **IEEEXtreme 20.0** (CSAcademy), con sus ejemplos de entrada/salida y una captura de la página original para verificar que el contenido coincide.

**Sitio web:** https://rechashhh.github.io/ieeextreme20-tareas/ — enunciados con fórmulas, vista "Comparar lado a lado" con el original y descargas (.zip por tarea o todo junto).

## Tareas

| # | Tarea | Tipo | Tiempo (base) | Memoria | Puntos |
|---|---|---|---|---|---|
| 01 | [Welcome to IEEEXtreme 20.0](problemas/01-welcome-to-ieeextreme-20/enunciado.md) | Estándar | 1000 ms | 256 MB | 100.00 |
| 02 | [Even Signal Windows](problemas/02-even-signal-windows/enunciado.md) | Estándar | 2000 ms | 256 MB | 51.88 |
| 03 | [Lunar Giant](problemas/03-lunar-giant/enunciado.md) | Estándar | 1000 ms | 256 MB | 80.06 |
| 04 | [IEEE Global Expert Selection Challenge](problemas/04-ieee-global-expert-selection-challenge/enunciado.md) | Estándar | 4000 ms | 256 MB | 75.73 |
| 05 | [Shroud](problemas/05-shroud/enunciado.md) | Juego contra bots | 4000 ms | 256 MB | 77.03 |
| 06 | [Encrypted Thresholds](problemas/06-encrypted-thresholds/enunciado.md) | Estándar | 1000 ms | 256 MB | 64.91 |
| 07 | [Clue Duel](problemas/07-clue-duel/enunciado.md) | Juego contra bots | 1000 ms | 256 MB | 66.88 |
| 08 | [One Junction Box](problemas/08-one-junction-box/enunciado.md) | Estándar | 1000 ms | 256 MB | 69.73 |
| 09 | [Monotone Tree](problemas/09-monotone-tree/enunciado.md) | Estándar | 1000 ms | 256 MB | 69.37 |
| 10 | [At Most One Cover](problemas/10-at-most-one-cover/enunciado.md) | Estándar | 2000 ms | 256 MB | 66.87 |
| 11 | [Overclock in Night City](problemas/11-overclock-in-night-city/enunciado.md) | Estándar | 1000 ms | 256 MB | 67.79 |
| 12 | [Rooted Vector](problemas/12-rooted-vector/enunciado.md) | Estándar | 1000 ms | 256 MB | 72.50 |
| 13 | [Auction Duel](problemas/13-auction-duel/enunciado.md) | Juego contra bots | 2000 ms | 256 MB | 83.02 |
| 14 | [A Blueprint or a Schedule](problemas/14-a-blueprint-or-a-schedule/enunciado.md) | Estándar | 1000 ms | 256 MB | 74.24 |
| 15 | [Two Networks, One Emergency](problemas/15-two-networks-one-emergency/enunciado.md) | Estándar | 1000 ms | 256 MB | 78.93 |
| 16 | [Dots and Boxes](problemas/16-dots-and-boxes/enunciado.md) | Juego contra bots | 2000 ms | 256 MB | 89.26 |
| 17 | [Flip 7](problemas/17-flip-7/enunciado.md) | Interactiva | 1000 ms | 256 MB | 74.34 |
| 18 | [Deliveries in the Kingdom](problemas/18-deliveries-in-the-kingdom/enunciado.md) | Estándar | 1000 ms | 256 MB | 75.91 |
| 19 | [Clockwise Checkpoints](problemas/19-clockwise-checkpoints/enunciado.md) | Estándar | 1000 ms | 256 MB | 72.97 |
| 20 | [Typo Bowl](problemas/20-typo-bowl/enunciado.md) | Estándar | 1000 ms | 256 MB | 76.75 |

> **Tiempo (base):** límite oficial del juez. La web de CSAcademy muestra un límite mayor según el lenguaje del editor (por ejemplo 2500 ms en Python cuando el base es 1000 ms).

## Estructura

```
problemas/NN-nombre/
  enunciado.md        enunciado en Markdown estándar (con fórmulas $...$)
  enunciado.csa.txt   markup original de CSAcademy, sin modificar
  original.png        captura del enunciado en la página original
  ejemplos/           sampleK.in / sampleK.out
  adjuntos/           archivos adjuntos del enunciado (solo Lunar Giant)
  meta.json           límites, tipo de tarea, puntos y ejemplos
site/template.html    plantilla del sitio
tools/                convertidor de markup y generador del sitio
```

En las tareas de juego (Shroud, Clue Duel, Auction Duel, Dots and Boxes) los archivos `.out` están vacíos: la interacción con el juez se explica dentro del enunciado.

## Generar el sitio localmente

```
python tools/build_site.py
```

El resultado queda en `_site/`. GitHub Actions lo publica automáticamente en GitHub Pages en cada push a `main`.

---
Los enunciados pertenecen a IEEE / IEEEXtreme y a sus autores. Este repositorio es una recopilación con fines educativos.
