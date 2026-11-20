# Deliveries in the Kingdom

**Tipo:** Estándar · **Límite de tiempo:** 1000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring

Pedro was playing Minecraft and received a quest: make wood deliveries between cities of the kingdom.

However, an Enderman is trying to disrupt his quest. On each delivery, the Enderman is in a specific city and Pedro wants to avoid passing through that city along his route.

To get around, Pedro uses the kingdom's rail system. He has a map showing which cities are connected by bidirectional rails.

For each delivery, Pedro receives three pieces of information:

- The city where he must chop the trees (source);
- The city where he must deliver the wood (destination);
- The city where the Enderman is located.

Pedro wants to know whether it is possible to make the delivery **without passing through the city where the Enderman is**.

## Problem

Given the map of the kingdom and several delivery queries, determine for each of them whether there is a path from the source city to the destination city that **does not pass through the city where the Enderman is**.

## Standard input

The first line contains two integers $N$ and $M$, the number of cities and the number of rails.

Each of the next $M$ lines contains two integers $A$ and $B$, indicating that there is a bidirectional rail between cities $A$ and $B$.

The next line contains an integer $Q$, the number of deliveries.

Each of the next $Q$ lines contains three integers:

- $C$, the city where Pedro must chop the tree (source);
- $D$, the city where he must deliver the wood (destination);
- $E$, the city where the Enderman is located.

## Standard output

For each delivery, print:

- `Sim` (Yes in portuguese) if it is possible to make the delivery without passing through the Enderman's city;
- `Nao` (No in portuguese) otherwise.

## Constraints and notes

- $N + M \le 10^5$.
- $1 \le Q \le 10^5$.
- Cities are numbered from $1$ to $N$.
- Rails are bidirectional.
- $1 \le A, B, C, D, E \le N$.
- Pedro ***cannot pass*** through the city where the Enderman is, neither as an intermediate city nor as the source or destination.
- Each delivery must be analyzed independently.

### Ejemplo 1

Entrada:

```
4 4
1 2
2 3
3 4
1 4
3
1 3 2
1 3 4
2 4 1
```

Salida:

```
Sim
Sim
Sim
```

Explicación:

In this example, each delivery has a route that avoids the specified city.

### Ejemplo 2

Entrada:

```
6 5
1 2
2 3
3 4
4 5
3 6
2
1 6 4
1 5 3
```

Salida:

```
Sim
Nao
```

Explicación:

In this example, the first delivery can follow $1 \to 2 \to 3 \to 6$, avoiding city $4$. In the second delivery, city $3$ is an articulation point: every path from $1$ to $5$ passes through it.

If $C=D$ and $C\ne E$, the answer is `Sim`: Pedro is already at the destination and does not need to traverse any railway connections.
