# Dots and Boxes

**Tipo:** Juego contra bots · **Límite de tiempo:** 2000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring

**Dots and Boxes** is a two-player pencil-and-paper game. Your program plays one side against an opponent program, with a judge relaying messages between them over standard input and standard output.

The board is a grid of $R \times C$ boxes, drawn as $(R + 1) \times (C + 1)$ dots. A dot is named by its row, from $0$ to $R$ top to bottom, and its column, from $0$ to $C$ left to right. The game doesn't start from an empty board: some lines are already drawn, and a box whose four sides are already drawn at the start belongs to nobody and is out of play.

The players take turns drawing a line between two dots next to each other, horizontally or vertically, that aren't joined yet. **A player who draws the fourth side of a box takes it, and has to draw another line.** A line can complete two boxes at once, and taking a box always gives another turn, even if it is the last line of a chain of them. The game ends when every line is drawn, and the player with more boxes wins.

A match consists of games against each of the judges' bots, on boards of different sizes and starting positions. Your program is started anew for every game. Sometimes you draw the first line, sometimes your opponent does.

## Input

All messages from the judge arrive on standard input, one per line. Tokens on a line are separated by single spaces.

A game starts with the size of the board and whether you draw the first line, followed by the starting position as $2R + 1$ rows of $2C + 1$ characters each:

```
GAME <R> <C> <first>
<row 0>
...
<row 2R>
```

- $1 \le R, C \le 10$ 
- `<first>` is `1` if you draw the first line, and `0` if your opponent does.
- Row $2i$ of the position describes the dots of row $i$ and the horizontal lines between them: a `+` for every dot, and between two dots a `-` if the line is drawn, or a `.` if it isn't.
- Row $2i + 1$ describes the vertical lines from the dots of row $i$ down to row $i + 1$, and the boxes between them: a `|` for a drawn line, a `.` for an undrawn one, and for every box a `#` if its four sides are drawn, or an `o` if they aren't.
- No box has exactly three sides drawn at the start, and at least one line isn't drawn.

Then the judge sends, in the order they happen:

```
YOUR_TURN
OPPONENT <r1> <c1> <r2> <c2>
```

`YOUR_TURN` asks you to draw a line (see Output). `OPPONENT` tells you a line your opponent drew, between the dots $(r_1, c_1)$ and $(r_2, c_2)$, with the upper or left dot first. You are never told which boxes were taken: you can work that out from the lines.

After the last line, or when a player breaks the rules, you get:

```
GAME_END <points>
```

`<points>` is the number of points you earned for this game, with two decimals (see Scoring). Your program should exit after reading `GAME_END`.

## Output

Write exactly one line to standard output for each `YOUR_TURN`, then flush the output and wait for the next line. Don't print anything at any other time.

```
LINE <r1> <c1> <r2> <c2>
```

The two dots have to be next to each other, horizontally or vertically, in either order, and the line between them can't be drawn yet.

## Scoring

What counts is how far ahead of your opponent you finish, not only whether you win, measured against the $N$ boxes that are in play: those not complete at the start. A game earns you

$5 + 10 \cdot \frac{\text{your boxes} - \text{opponent's boxes}}{N}$ 

points, but never less than $0$ or more than $10$. A tie earns $5$ points, and finishing ahead by half of the boxes in play, or more, earns $10$.

A player that breaks the rules forfeits the game: 0 points for them, 10 for their opponent. Breaking the rules means drawing a line that isn't allowed, printing an invalid line, crashing, or going over the time or memory limit, which apply to each game separately.

Your score is proportional to the average of your points over the games.

## Example

A game on a board of $2 \times 2$ boxes, where you draw the first line. The top-left box is complete already, so $N = 3$ boxes are in play. The judge's messages, with your answers after each `YOUR_TURN`:

```
GAME 2 2 1
+-+.+
|#|o.
+-+-+
.o.o.
+.+.+
YOUR_TURN
                LINE 1 1 2 1
OPPONENT 0 1 0 2
YOUR_TURN
                LINE 0 2 1 2
YOUR_TURN
                LINE 2 0 2 1
OPPONENT 1 0 2 0
OPPONENT 2 1 2 2
YOUR_TURN
                LINE 1 2 2 2
GAME_END 8.33
```

1. The top-right box starts with its left and bottom sides, and the two bottom boxes with their tops. You draw the line between the bottom boxes, after which every box in play has two sides, so any line gives a box away.
2. Your opponent draws the top of the top-right box, its third side. You complete it with its right side, take it, and have to draw again: the bottom of the bottom-left box, which is its third side.
3. Your opponent completes the bottom-left box with its left side, takes it, and has to draw again: the bottom of the bottom-right box, its third side.
4. You complete the bottom-right box with its right side. Two boxes to one, of three in play, is $5 + 10 \cdot \frac{1}{3} = 8.33$ points.
