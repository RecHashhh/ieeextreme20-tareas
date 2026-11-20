# Lunar Giant

**Tipo:** Estándar · **Límite de tiempo:** 1000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring
**Adjuntos:** [transitions.tsv](adjuntos/transitions.tsv)

Your task is to produce the same output as the program encoded in the attached [transition table](https://publicmedia1.csacademy.com/public/transitions.tsv).

## Standard input

The first line of input contains an integer $N$.

Each line of the next $N$ lines of the input is a testcase.

A testcase is a list of space separated integers $C_1, \ldots, C_k$.

## Standard output

A single integer per each one of the $N$ testcases.

## Constraints and notes

- $1 \le N \le 10$.
- $0 \le C_i \le 1000$.
- $10\%$ of the test cases are easy: with a single number $C_1 < 25$ per testcase.
- $40\%$ of the test cases are medium: $C_i < 25$.
- $50\%$ of the test cases are hard: with no restriction other than the constraints above.

### Ejemplo 1

Entrada:

```
5
1
3
5
8
13
```

Salida:

```
148
45
68
208
195
```

### Ejemplo 2

Entrada:

```
5
34
55 89
233 610
0 0 0 0 144
987
```

Salida:

```
158
195
73
0
122
```

### Ejemplo 3

Entrada:

```
5
0 5
5 0
13 1 1
21 21 34
2 3 5 8 13
```

Salida:

```
81
68
139
127
147
```
