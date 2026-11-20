# Clue Duel

**Tipo:** Juego contra bots · **Límite de tiempo:** 1000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring

**Clue Duel** is a two-player deduction game based on the classic board game Clue (Cluedo). Your program plays one seat at the table against an opponent program, with a judge relaying messages between them over standard input and standard output.

The deck has three categories of cards: persons `P1` to `PA`, weapons `W1` to `WB` and locations `L1` to `LC`. The numbers $A$, $B$ and $C$ differ from game to game and are always odd. At the start of a game the deck is shuffled and dealt: one card of each category, which nobody sees, is the **solution**, and the rest of each category is split evenly between the two players, so each of you holds $\frac{A - 1}{2}$ persons, $\frac{B - 1}{2}$ weapons and $\frac{C - 1}{2}$ locations. Your goal is to deduce the solution before your opponent does.

Play alternates turns. On your turn you either:

- **Guess** a person, a weapon and a location. Your opponent must reveal one matching card from their hand if they hold one (their choice, if more than one matches), or report that they cannot disprove the guess.
- **Accuse** a person, a weapon and a location as the final solution.

When your opponent guesses on their turn, your program is asked to disprove the guess the same way, if it can.

**The game ends the instant either player makes an accusation**, correct or not. If nobody accuses within the game's number of turns, the game ends and neither player gets any points.

A match consists of games against each of the judges' bots, with different decks. Every deal is played twice, once with each player moving first and the hands exchanged, so you make the first move in half of the games. Your program is started anew for every game.

## Input

All messages from the judge arrive on standard input, one per line. Tokens on a line are separated by single spaces.

A game starts with the deck and the number of turns, then your hand, in no particular order:

```
GAME <A> <B> <C> <turns>
HAND <c1> <c2> ... <cn>
```

- $3 \le A, B, C \le 41$, all odd, and $2 \le turns \le 1000$. The turns are counted for both players together.

Then one of the following lines arrives, repeating until the game ends.

It's your turn:

```
TURN YOU
```

Answer with `GUESS` or `ACCUSE` (see Output). If you guessed, the judge follows up with one of these before the next prompt:

```
RESULT SHOWN <card>
RESULT NONE
```

`RESULT SHOWN <card>` gives the card your opponent revealed to disprove your guess. `RESULT NONE` means your opponent held none of the three cards you guessed.

Your opponent guessed on their turn:

```
TURN OPP GUESS <person> <weapon> <location>
```

Answer with `SHOW` or `NONE` (see Output).

When your opponent accuses, you get no prompt, and the next line is the end of the game:

```
GAME_END <accuser> <verdict> <points>
```

- `<accuser>` is `YOU` or `OPP`, the player who made the game ending accusation, or `NONE` if the game ended after its last turn.
- `<verdict>` is `CORRECT` or `INCORRECT`, whether the accusation matched the solution. It is `FORFEIT` when `<accuser>` is `OPP` and your opponent broke the rules, and `NONE` if the game ended after its last turn.
- `<points>` is the number of points you earned for this game.

Your program should exit after reading `GAME_END`.

## Output

Write exactly one line to standard output for each `TURN YOU` or `TURN OPP GUESS` prompt, then flush the output and wait for the next line. Don't print anything at any other time.

To answer `TURN YOU`, either guess or accuse with a person, a weapon and a location, for example `GUESS P2 W3 L5`. Any valid codes may be used, including cards in your own hand. An accusation immediately ends the game.

```
GUESS <person> <weapon> <location>
ACCUSE <person> <weapon> <location>
```

To answer `TURN OPP GUESS`, reveal one card from your hand that was part of the guess, or report that you hold none of the three:

```
SHOW <card>
NONE
```

## Scoring

Each game's outcome depends only on who accused and whether they were right:

- You accuse correctly: 10 points
- You accuse incorrectly: 3 points
- Your opponent accuses correctly: 0 points
- Your opponent accuses incorrectly: 7 points
- Nobody accuses within the game's turns: 0 points

A player that breaks the rules forfeits the game: 0 points for them, 10 for their opponent. Breaking the rules means printing an invalid line, showing a card you don't hold or that wasn't guessed, answering `NONE` while holding a guessed card, crashing, or going over the time or memory limit, which apply to each game separately.

Your score is proportional to the average of your points over the games.

## Example

The judge's messages for one game, with the classic deck of $5$ persons, $7$ weapons and $9$ locations:

```
GAME 5 7 9 100
HAND P1 P2 W1 W2 W3 L1 L2 L3 L4
TURN YOU
RESULT SHOWN P3
TURN OPP GUESS P1 W6 L2
TURN YOU
RESULT NONE
TURN OPP GUESS P2 W1 L8
TURN YOU
GAME_END YOU CORRECT 10
```

Your program's answers, in order:

```
GUESS P3 W4 L5
SHOW P1
GUESS P5 W7 L9
SHOW W1
ACCUSE P5 W7 L9
```

1. You're dealt `P1 P2 W1 W2 W3 L1 L2 L3 L4`: $2$ persons, $3$ weapons and $4$ locations, as is your opponent, and the $3$ cards left over are the solution.
2. You guess `P3 W4 L5`, and your opponent shows you `P3`: it isn't the solution's person.
3. Your opponent guesses `P1 W6 L2`. You hold both `P1` and `L2`, and choose to show `P1`.
4. You guess `P5 W7 L9`, and get `RESULT NONE`. You don't hold any of these cards either, so they are the solution.
5. Your opponent guesses `P2 W1 L8`. You hold `P2` and `W1`, and show `W1`.
6. You accuse `P5 W7 L9`, which is correct and ends the game with 10 points for you.
