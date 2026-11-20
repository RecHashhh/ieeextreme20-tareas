# Rooted Vector

**Tipo:** Estándar · **Límite de tiempo:** 1000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring

You are given a tree with $n$ vertices rooted at vertex $1$. Each vertex $v$ has an integer vector $(a_v, b_v)$.

Choose a set $S$ containing the root such that whenever a vertex is selected, all of its ancestors are also selected. Selecting all its descendants is not required.

Let $A$ and $B$ be the sums of the first and second coordinates of the selected vectors. Maximize $A^2 + B^2$.

## Standard input

The first line contains $n$.

The $v$-th of the next $n$ lines contains three integers $p_v$, $a_v$ and $b_v$, where $p_v$ is the parent of $v$.

## Standard output

Print one integer: the maximum value of $A^2 + B^2$. The answer may exceed the range of a signed $64$-bit integer.

## Constraints and notes

- $1 \le n \le 5000$.
- $-10^6 \le a_v, b_v \le 10^6$.
- The root has $p_1 = 0$. All other parent identifiers are between $1$ and $n$, and form a tree rooted at $1$.
- Labels need not be in topological order.

### Ejemplo 1

Entrada:

```
3
0 1 0
1 -3 0
1 0 2
```

Salida:

```
8
```

### Ejemplo 2

Entrada:

```
3
0 1 1
1 0 -20
1 0 3
```

Salida:

```
362
```
