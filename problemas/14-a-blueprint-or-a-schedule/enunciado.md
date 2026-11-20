# A Blueprint or a Schedule

**Tipo:** Estándar · **Límite de tiempo:** 1000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring

A laboratory has $n$ modules and $m$ one-way connections. These connections contain no directed cycle.

You also have a blueprint with $k$ parts and $k-1$ one-way connections. Ignoring directions, the blueprint is a tree.

The laboratory accepts either of these two deliverables:

- ***An assembly:*** assign the $k$ parts to distinct modules so that every blueprint connection exists between the assigned modules, with the same direction. Additional connections between these modules are allowed.
- ***A schedule:*** assign each module a time slot from $1$ to $k-1$ so that the endpoints of every connection have different slots.

Construct either deliverable. At least one always exists. If both exist, either is accepted. Providing a schedule does not assert that an assembly is impossible.

## Standard input

The first line contains $n$, $m$, and $k$.

The next $m$ lines contain $u$ and $v$, describing a connection from module $u$ to module $v$.

The next $k-1$ lines contain $a$ and $b$, describing a blueprint connection from part $a$ to part $b$.

## Standard output

For an assembly, print `TREE` on the first line. On the second line, print $k$ distinct module identifiers $p_1, \ldots, p_k$. Each blueprint connection $a \to b$ must have a corresponding connection $p_a \to p_b$.

For a schedule, print `COLOR` on the first line. On the second line, print $n$ integers between $1$ and $k-1$, the slots of all modules. This option is unavailable when $k=1$.

## Constraints and notes

- $1 \le n \le 20\,000$.
- $0 \le m \le 10^{6}$.
- $1 \le k \le 200$. The value of $k$ may exceed $n$.
- $1 \le u, v \le n$ and $u \ne v$.
- Connections are distinct and form a directed acyclic graph.
- $1 \le a, b \le k$ and $a \ne b$.
- The underlying undirected graph of the blueprint is a tree.

### Ejemplo 1

Entrada:

```
3 3 3
1 2
1 3
2 3
2 1
2 3
```

Salida:

```
TREE
3 1 2 
```

### Ejemplo 2

Entrada:

```
3 2 3
1 2
1 3
1 2
2 3
```

Salida:

```
COLOR
1 2 2 
```

### Ejemplo 3

Entrada:

```
1 0 1
```

Salida:

```
TREE
1 
```
