# Typo Bowl

**Tipo:** Estándar · **Límite de tiempo:** 1000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring

The Super Bowl was recently played, the event that marks the final of the American football championship in the United States. Traditionally, there are shows both at the opening and at halftime.

However, this edition had something curious happen: when announcing the opening band "Green Day", due to a typo, the participation of "Green Bay" was announced, which coincidentally is a team in the league.

Seeing the reaction, the league commissioner decided to create the **Typo Bowl**, an event in which:

- the **AFC** team most similar to the opening show band faces.
- the **NFC** team most similar to the halftime show band.

The similarity between a band name and a team name is defined as the **minimum number of operations needed to transform the band name into the team name**. The smaller this number, the greater the similarity.

The allowed operations are:

- Change a character to another one.
- Remove a character.
- Add a character.

Help the commissioner determine the matchup for the Typo Bowl.

## Standard input

The first line contains an integer $N$, the number of teams in the AFC and in the NFC.

The second line contains the name of the opening show band.

The next $N$ lines contain the names of the AFC teams.

The next line contains the name of the halftime show band.

The next $N$ lines contain the names of the NFC teams.

Each name is a non-empty string that may contain spaces, and it is case-sensitive.

## Standard output

Print the names of the two teams that will play the Typo Bowl, in the following format:

`<AFC> x <NFC>`

If there is a tie for the smallest distance, choose the team whose name appears first in the input (this applies separately to the AFC and to the NFC).

## Constraints and notes

- $1 \le N \le 16$.
- Every name has length between $1$ and $10^3$.

### Ejemplo 1

Entrada:

```
2
Green Day
Green Bay
Dallas Cowboys
The Weeknd
Minnesota Vikings
New York Giants
```

Salida:

```
Green Bay x Minnesota Vikings
```

### Ejemplo 2

Entrada:

```
3
ABC
ABD
AB
AABC
XYZ
XYY
XY
```

Salida:

```
ABD x XYZ
```
