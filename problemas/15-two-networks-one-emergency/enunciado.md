# Two Networks, One Emergency

**Tipo:** Estándar · **Límite de tiempo:** 1000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring

A country has $n$ cities and two transportation networks. Each network connects all cities with $n-1$ bidirectional connections and forms a tree. Each connection has a nonnegative travel time. The two networks may have different connections and travel times.

Each city has an emergency station, initially switched off.

A drill between two distinct cities $u$ and $v$ with active stations consists of traveling from $u$ to $v$ using the first network, then returning from $v$ to $u$ using the second. In each network, the unique path between the two cities is followed. The total drill time is therefore $d_1(u,v) + d_2(u,v)$, where $d_t(u,v)$ is the sum of the travel times along the path between $u$ and $v$ in network $t$.

There will be $q$ operations. Each operation specifies a city: if its station is off, it is switched on; if it is on, it is switched off.

After each operation, find the largest total drill time between two distinct active stations. If fewer than two stations are active, output $-1$.

## Standard input

The first line contains two integers $n$ and $q$.

The next $n-1$ lines describe the first network. Each contains three integers $u$, $v$ and $w$, describing a bidirectional connection between cities $u$ and $v$ with travel time $w$.

The next $n-1$ lines describe the second network in the same format. Each network is guaranteed to be a tree.

The next $q$ lines each contain an integer $v$, the city whose station changes state. A city may appear any number of times.

## Standard output

Print $q$ lines. On line $i$, print the answer after operation $i$.

## Constraints and notes

- $1 \le n, q \le 100\,000$.
- $1 \le u, v \le n$ and $u \ne v$.
- $0 \le w \le 10^9$.
- $1 \le v \le n$ for each operation.

### Ejemplo 1

Entrada:

```
3 7
1 2 2
2 3 1
1 3 4
3 2 1
1
2
3
1
2
3
2
```

Salida:

```
-1
7
7
2
-1
-1
-1
```
