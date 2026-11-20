# Encrypted Thresholds

**Tipo:** Estándar · **Límite de tiempo:** 1000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring

An emergency network consists of $n$ stations connected by $n-1$ bidirectional links, so there is exactly one simple path between every pair of stations. Each link has a non-negative integer encryption code.

For two distinct stations $u$ and $v$, define $X(u,v)$ as the bitwise XOR of the codes on the unique path from $u$ to $v$.

You are given $q$ independent threshold queries. For each threshold $k$, find the number of unordered pairs of distinct stations $\{u, v\}$ such that

$X(u,v) < k$.

## Standard input

The first line contains two integers $n$ and $q$.

Each of the next $n-1$ lines contains three integers $u$, $v$ and $w$, describing a link between stations $u$ and $v$ with encryption code $w$.

Each of the next $q$ lines contains one integer $k$.

## Standard output

For every query, print the required number of unordered pairs on its own line.

## Constraints and notes

- $2 \le n, q \le 200\,000$.
- $1 \le u, v \le n$.
- $0 \le w < 2^{20}$.
- $0 \le k \le 2^{20}$.

### Ejemplo 1

Entrada:

```
4 5
1 2 3
2 3 5
2 4 6
0
1
4
8
1048576
```

Salida:

```
0
0
2
6
6
```

Explicación:

In this example, the path XOR values of the six unordered pairs are $3, 6, 5, 5, 6, 3$. Therefore, two pairs have value less than $4$, and all six have value less than $8$.
