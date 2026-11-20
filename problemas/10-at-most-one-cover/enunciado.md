# At Most One Cover

**Tipo:** Estándar · **Límite de tiempo:** 2000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring

There is a strip of $m$ cells numbered from $1$ to $m$ from left to right. You are given $n$ segments. The $j$-th segment is described by four integers $l_j, r_j, p_j, q_j$. It covers all cells from $l_j$ to $r_j$ inclusive and exists with probability $\frac{p_j}{q_j}$. All segments exist independently of each other.

For each cell $i$ from $1$ to $m$, find the probability that cell $i$ is covered by at most one of the existing segments.

It can be shown that each answer can be written as an irreducible fraction $\frac{x}{y}$ where $y \not\equiv 0 \pmod{998244353}$. Print $x \cdot y^{-1} \bmod 998244353$.

## Standard input

The first line contains two integers $n$ and $m$.

The $j$-th of the next $n$ lines contains four integers $l_j, r_j, p_j, q_j$.

## Standard output

Print $m$ integers. The $i$-th of them should be the answer for cell $i$ modulo $998244353$.

## Constraints and notes

- $1 \le n, m \le 2 \cdot 10^5$.
- $1 \le l_j \le r_j \le m$.
- $0 \le p_j \le q_j$.
- $1 \le q_j < 998244353$.

### Ejemplo 1

Entrada:

```
2 3
1 2 1 2
2 3 1 2
```

Salida:

```
1 249561089 1
```

Explicación:

In this example, cells 1 and 3 are covered by only one segment, so the answer for them is $1$. Cell 2 is covered by two segments, and the bad case is when both of them exist, so the answer is $1 - \frac{1}{4} = \frac{3}{4}$.

### Ejemplo 2

Entrada:

```
3 5
1 3 1 1
3 5 2 3
2 2 7 7
```

Salida:

```
1 0 332748118 1 1
```

Explicación:

In this example, the first and the third segments always exist. Cell 2 is covered by both of them, so the answer is $0$. Cell 3 is always covered by the first segment, so the second segment must not exist, which happens with probability $\frac{1}{3}$.

### Ejemplo 3

Entrada:

```
3 4
1 4 1 2
2 3 1 3
3 4 1 4
```

Salida:

```
1 831870295 956650839 124780545
```

Explicación:

In this example, the answers are $1$, $\frac{5}{6}$, $\frac{17}{24}$ and $\frac{7}{8}$.
