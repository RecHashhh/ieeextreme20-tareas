# Monotone Tree

**Tipo:** Estándar · **Límite de tiempo:** 1000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring

You are given a tree with $n$ vertices rooted at vertex $1$. Each vertex $v$ has an integer value $a_v$ and a positive integer weight $w_v$.

Assign a real number $x_v$ to each vertex. The value of a parent must not exceed the value of any of its children. Among all valid assignments, minimize

$\sum_{v=1}^{n} w_v (x_v - a_v)^2.$

Output the optimal assignment. It can be proved that it is unique and all its values are rational.

## Standard input

The first line contains $n$.

The $v$-th of the next $n$ lines contains three integers $p_v$, $a_v$ and $w_v$: the parent, value, and weight of vertex $v$.

## Standard output

Print $n$ lines. Line $v$ must contain two integers $b_v$ and $c_v$ such that $x_v = \frac{b_v}{c_v}$, $c_v > 0$, and $\gcd(|b_v|, c_v) = 1$. Represent zero as `0 1`.

## Constraints and notes

- $1 \le n \le 200\,000$.
- $-10^6 \le a_v \le 10^6$.
- $1 \le w_v \le 10^6$.
- For the root, $p_1 = 0$. For all other vertices, $1 \le p_v \le n$.
- The parent pointers form a tree rooted at $1$; labels need not be in topological order.
- The optimal values admit representations with $|b_v| \le 2 \cdot 10^{17}$ and $c_v \le 2 \cdot 10^{11}$.

### Ejemplo 1

Entrada:

```
3
0 4 1
1 0 2
1 8 1
```

Salida:

```
4 3
4 3
8 1
```

### Ejemplo 2

Entrada:

```
1
0 -1000000 1000000
```

Salida:

```
-1000000 1
```
