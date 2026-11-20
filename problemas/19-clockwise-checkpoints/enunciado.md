# Clockwise Checkpoints

**Tipo:** Estándar · **Límite de tiempo:** 1000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring

A circular track has length $C$. Checkpoints are placed at distinct integer positions from $0$ to $C-1$. Starting at a checkpoint, you travel clockwise until you reach the next checkpoint. After the last checkpoint in clockwise order, the next checkpoint is the first one after wrapping around.

Find the longest such checkpoint-to-checkpoint segment. If several segments have the same length, choose the one whose starting checkpoint has the smallest position.

## Standard input

The first line contains two integers $n$ and $C$.

The second line contains $n$ distinct integers $p_1, p_2, \ldots, p_n$, the checkpoint positions. They may appear in any order.

## Standard output

Print two integers: the length of the longest clockwise segment and the position of its starting checkpoint.

## Constraints and notes

- $1 \le n \le 2\cdot 10^5$.
- $1 \le C \le 10^9$.
- $n \le C$.
- $0 \le p_i < C$ for each valid $i$.

If there is only one checkpoint, the segment starts there, goes once around the track, and has length $C$.

### Ejemplo 1

Entrada:

```
3 12
9 0 4
```

Salida:

```
5 4
```

### Ejemplo 2

Entrada:

```
2 10
6 1
```

Salida:

```
5 1
```
