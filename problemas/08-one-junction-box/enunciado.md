# One Junction Box

**Tipo:** Estándar · **Límite de tiempo:** 1000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring

The **Mechanic** is wiring up a new section of the world in **Terraria**. The section is a rectangular block of $N \times M$ tiles, with rows numbered from $1$ (top) to $N$ (bottom) and columns numbered from $1$ (left) to $M$ (right). The tile in row $r$ and column $c$ is denoted $(r, c)$.

Two tunnels are going to be dug through the block:

- The **Demolitionist** starts at the bottom-left tile $(N, 1)$ and blasts his way to the **Floating Island** at the top-right tile $(1, M)$. From tile $(r, c)$ he may only move to $(r-1, c)$ (up) or to $(r, c+1)$ (right).
- The **Steampunker** starts at the top-left tile $(1, 1)$ and lays a minecart track to the **Underworld Gate** at the bottom-right tile $(N, M)$. From tile $(r, c)$ she may only move to $(r+1, c)$ (down) or to $(r, c+1)$ (right).

Both the starting and ending tiles belong to the tunnel they are part of. It can be shown that the two tunnels always touch somewhere, even if the two travelers never meet at the same moment.

The Mechanic only has a single **Junction Box** in her inventory, so she is interested in layouts where the two tunnels share **exactly one tile**. Two layouts are different if the Demolitionist's tunnel or the Steampunker's track differs in at least one tile.

Given $N$ and $M$, count the number of layouts in which the two tunnels share exactly one tile. Since the answer can be very large, print it modulo $998\,244\,353$.

## Standard input

The only line contains two integers $N$ and $M$, the number of rows and columns of the block.

## Standard output

Print a single integer: the number of pairs of tunnels that share exactly one tile, modulo $998\,244\,353$.

## Constraints and notes

- $1 \le N, M \le 10^6$.

### Ejemplo 1

Entrada:

```
4 5
```

Salida:

```
168
```

### Ejemplo 2

Entrada:

```
6 7
```

Salida:

```
40480
```
