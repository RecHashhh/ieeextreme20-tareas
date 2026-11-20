# Even Signal Windows

**Tipo:** Estándar · **Límite de tiempo:** 2000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring

A sensor records a binary signal as a string $S$. A window is a nonempty contiguous substring. A window is stable if it contains an even number of 1 characters.

For each query $[l, r]$, count the stable windows contained entirely in the substring $S[l\ldots r]$. Queries are independent.

## Standard input

The first line contains two integers $N$ and $Q$.

The second line contains a binary string $S$ of length $N$.

Each of the next $Q$ lines contains two integers $l$ and $r$. Positions are 1-indexed.

## Standard output

For each query, print one integer: the number of stable windows contained in $S[l\ldots r]$.

## Constraints and notes

- $1 \leq N, Q \leq 200000$.
- $1 \leq l \leq r \leq N$.

A window containing zero 1 characters is stable.

### Ejemplo 1

Entrada:

```
5 3
10110
1 5
2 4
3 3
```

Salida:

```
7
3
0
```

### Ejemplo 2

Entrada:

```
4 3
0000
1 4
2 3
4 4
```

Salida:

```
10
3
1
```
