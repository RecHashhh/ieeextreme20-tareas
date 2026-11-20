# Shroud

**Tipo:** Juego contra bots · **Límite de tiempo:** 4000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring

**Shroud** is a two-player game of painting territory in the fog. Your program plays one side against an opponent program, with a judge relaying messages between them over standard input and standard output.

The map is a grid of $R \times C$ cells, each a wall or open. Rows are numbered from $0$ at the top and columns from $0$ at the left. The open cells form one connected region, and the map looks the same turned by a half turn, so both players get the same terrain. Each player has $U$ units, numbered from $0$ to $U - 1$, starting in opposite corners.

The game lasts $T$ rounds. In each round, both players order every one of their units to move one cell north, east, south or west, or to hold, and all units move at the same time. A unit ordered into a wall or off the map holds. Units never share a cell: all units ordered into the same cell hold, two units ordered to swap cells hold, and a unit ordered into a cell whose unit ends up holding holds too. After moving, every unit paints the cell it stands on in its player's colour, over the other player's paint if the cell had it.

You don't see the whole board. Each round you are shown, for each of your units, the cells within $V$ steps of it in every direction: a square of $2V + 1$ by $2V + 1$ cells. In some games the walls of the map are given at the start; in the others you discover them as you go. Anything outside your units' views, including what your opponent has painted since you last looked, you have to remember or guess.

A match consists of games against each of the judges' bots, on different maps. Your program is started anew for every game.

## Input

All messages from the judge arrive on standard input, one per line. Tokens on a line are separated by single spaces.

A game starts with its parameters:

```
GAME <R> <C> <U> <V> <T> <known>
```

- $5 \le R, C \le 60$, $1 \le U \le 8$, $1 \le V \le 5$, $1 \le T \le 500$.
- If `<known>` is `1`, the map follows, as a line `MAP` and then $R$ lines of $C$ characters, `#` for a wall and `.` for an open cell. If it is `0`, nothing follows.

Then, for each round:

```
ROUND <n> <cells>
UNIT <i> <r> <c>
<2V + 1 lines of 2V + 1 characters>
...
```

`<n>` is the round number, from $1$, and `<cells>` the number of cells painted in your colour. Then, for each of your units in order, its number and the row and column it stands on, followed by its view: the $2V + 1$ rows from $r - V$ to $r + V$, each with the columns from $c - V$ to $c + V$. A character is `#` for a wall or a cell outside the map, `.` for an open cell nobody has painted, `+` for a cell painted in your colour, `-` for one painted in your opponent's, `M` for one of your units and `E` for an opponent's unit. Answer with your orders (see Output).

After the last round, or when a player breaks the rules, you get:

```
GAME_END <points>
```

`<points>` is the number of points you earned for this game, with two decimals (see Scoring). Your program should exit after reading `GAME_END`.

## Output

Write exactly one line to standard output for each `ROUND`, then flush the output and wait for the next line. Don't print anything at any other time.

```
ORDERS <d0> <d1> ... <dU-1>
```

`<di>` is the order for unit $i$: `N`, `E`, `S` or `W` to move, or `H` to hold.

## Scoring

What counts is how far ahead of your opponent you finish, not only whether you win. With $S$ the number of open cells of the map, a game earns you

$5 + 10 \cdot \frac{\text{your cells} - \text{opponent's cells}}{S}$ 

points, but never less than $0$ or more than $10$. A tie earns $5$ points, and finishing ahead by half of the open cells, or more, earns $10$.

A player that breaks the rules forfeits the game: 0 points for them, 10 for their opponent. Breaking the rules means printing an invalid line, crashing, or going over the time or memory limit, which apply to each game separately. An order that cannot be carried out is not a mistake: the unit holds.

Your score is proportional to the average of your points over the games.

## Example

The judge's messages for one game, with your answers after each round:

```
GAME 6 6 1 1 4 1
MAP
######
#...##
#...##
##...#
##...#
######
ROUND 1 1
UNIT 0 1 1
###
#M.
#..
                ORDERS E
ROUND 2 2
UNIT 0 1 2
###
+M.
...
                ORDERS S
ROUND 3 3
UNIT 0 2 2
++.
.M.
#.E
                ORDERS E
ROUND 4 3
UNIT 0 2 2
++.
.M.
#.E
                ORDERS S
GAME_END 5.83
```

1. A $6 \times 6$ map with $12$ open cells, given at the start, one unit per player, a view of $1$ step and $4$ rounds. Your unit starts at row $1$, column $1$, and your opponent's in the opposite corner, at row $4$, column $4$; each start cell is painted, so you have $1$ cell.
2. Your view shows walls above and to the left. You move east, to row $1$, column $2$, and paint it.
3. The view now shows your paint behind you. You move south, to row $2$, column $2$.
4. The view shows your opponent's unit at row $3$, column $3$. You order east, to row $2$, column $3$; your opponent orders north, to the same cell, so both units hold and nobody paints a new cell.
5. You move south to row $3$, column $2$, and your opponent east, to row $3$, column $4$. You finish with $4$ cells to $3$, out of $12$ open cells: $5 + 10 \cdot \frac{4 - 3}{12} = 5.83$ points.
