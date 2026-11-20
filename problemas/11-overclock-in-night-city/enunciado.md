# Overclock in Night City

**Tipo:** Estándar · **Límite de tiempo:** 1000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring

In the neon-drenched sprawl of **Night City**, the ripperdoc **Dr. Viktor Vektor** is about to install a **Sandevistan** into **David Martinez**. Every extra point of base rating makes the implant more dangerous, so Viktor wants the weakest model that still does the job.

To test it, **Lucy** loads a braindance training simulation with $N$ **Arasaka squads**. The $i$-th squad has $a_i$ soldiers. David and a simulated **Adam Smasher** take turns, and David moves first.

- **David's turn.** Let $k$ be the number of turns David has already taken ($k = 0$ on his first turn). He chooses a squad that still has soldiers and takes out between $1$ and $X + k$ of its soldiers, inclusive, where $X$ is the base rating of the Sandevistan. If the squad has fewer than $X + k$ soldiers, he may take out all of them. The overclock builds up with every activation, so David's limit grows by one each turn: $X$, then $X+1$, then $X+2$, and so on.
- **Smasher's turn.** He chooses any squad and calls in reinforcements, **doubling** its size: a squad with $z$ soldiers becomes a squad with $2z$ soldiers. Doubling an empty squad leaves it empty.

If all squads are empty right after David's turn, the simulation ends immediately.

This is a friendly training run, so nobody wins or loses. However, Smasher wants the simulation to last as long as possible, and it may even go on forever. David wants it to end. Both play optimally.

Viktor asks: what is the **minimum positive integer** $X$ such that David can force the simulation to end after a finite number of turns, no matter how Smasher plays?

It can be proven that such a value of $X$ always exists.

## Standard input

The first line contains an integer $N$, the number of squads.

The second line contains $N$ integers $a_1, a_2, \ldots, a_N$, the initial sizes of the squads.

## Standard output

Print a single integer, the minimum positive integer $X$ for which David can force the simulation to end.

## Constraints and notes

- $1 \le N \le 10^6$.
- $1 \le a_i \le 10^9$.

### Ejemplo 1

Entrada:

```
1
5
```

Salida:

```
2
```

Explicación:

In this example there is a single squad with $5$ soldiers. Below, $\xrightarrow{-t}$ means David takes out $t$ soldiers and $\xrightarrow{\times 2}$ means Smasher doubles the squad.

- With $X = 1$, the squad grows forever, even if David takes out as many soldiers as he can on every turn: $5 \xrightarrow{-1} 4 \xrightarrow{\times 2} 8 \xrightarrow{-2} 6 \xrightarrow{\times 2} 12 \xrightarrow{-3} 9 \xrightarrow{\times 2} 18 \xrightarrow{-4} \cdots$.
- With $X = 2$, the simulation ends after David's fourth turn: $5 \xrightarrow{-2} 3 \xrightarrow{\times 2} 6 \xrightarrow{-3} 3 \xrightarrow{\times 2} 6 \xrightarrow{-4} 2 \xrightarrow{\times 2} 4 \xrightarrow{-4} 0$.

### Ejemplo 2

Entrada:

```
3
5 1 5
```

Salida:

```
4
```

Explicación:

In this example, David can only touch one squad on his first turn, so one of the squads with $5$ soldiers is left untouched.

- With $X = 3$, David's next limit is only $4$. Smasher doubles that squad and keeps doubling it on every turn. Even if David spends every turn on it, it never empties: $5 \xrightarrow{\times 2} 10 \xrightarrow{-4} 6 \xrightarrow{\times 2} 12 \xrightarrow{-5} 7 \xrightarrow{\times 2} 14 \xrightarrow{-6} \cdots$.
- With $X = 4$, David takes out $4$ soldiers from one of the squads with $5$, leaving squads of sizes $1$, $1$ and $5$. It can be shown that from there David can force the simulation to end, no matter how Smasher plays.
