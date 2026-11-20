# Auction Duel

**Tipo:** Juego contra bots · **Límite de tiempo:** 2000 ms (base) · **Memoria:** 256 MB · **Puntuación:** Partial scoring

**Auction Duel** is a two-player sealed-bid auction game. Your program plays one side against an opponent program, with a judge relaying messages between them over standard input and standard output.

There are $K$ kinds of goods, numbered from $1$ to $K$, and each kind is auctioned exactly $M$ times, one copy per round, in an order the judge shuffles and neither player knows in advance. Both players start with the same amount of cash, which has to last the whole match: cash spent early is not there later, and cash left at the end counts in full.

Each player has a private value for each kind of good. The two players' values are permutations of the same list of $K$ distinct numbers: you are told your own values and the list, but not which good your opponent values at what. Your opponent's bids are your only clue.

Each round, one copy of a good comes up and both players bid for it at the same time, a whole number of cash from $0$ to what they have. Neither player sees the other's bid before making their own. The higher bid takes the good; if the bids are equal, a coin flip decides. What the winner pays depends on the pricing rule of the match:

- under the **second-price** rule, the winner pays the loser's bid;
- under the **first-price** rule, the winner pays its own bid.

The loser pays nothing, and both players then learn the other's bid.

A player that wins all $M$ copies of a good has its value for those copies raised by a bonus of $B$ percent. A player's total at the end is the value of the goods it won, bonuses included, plus its remaining cash.

A match consists of games against each of the judges' bots, with different goods, values, budgets, bonuses and pricing rules. Your program is started anew for every game.

## Input

All messages from the judge arrive on standard input, one per line. Tokens on a line are separated by single spaces.

A game starts with its parameters, then your values:

```
GAME <K> <M> <cash> <B> <rule>
VALUES <v1> <v2> ... <vK>
```

- $2 \le K \le 8$ kinds of goods, each auctioned $1 \le M \le 8$ times, for at most $60$ rounds in all.
- `<cash>` is what each player starts with, at most $10000$. `<B>` is the bonus, from $0$ to $200$ percent.
- `<rule>` is `second` or `first`.
- `<vi>` is your value for good $i$. The values are distinct, between $1$ and $1000$, and your opponent's values are a permutation of the same numbers.

Then, for each round:

```
ROUND <n> <good> <your cash> <opponent's cash>
```

`<n>` is the round number, from $1$, and `<good>` the kind of good up for auction. Answer with a bid (see Output). Once both players have bid, you get:

```
RESULT <won> <opponent's bid> <price>
```

`<won>` is `1` if you took the good and `0` if your opponent did, and `<price>` is what the winner paid.

After the last round, or when a player breaks the rules, you get:

```
GAME_END <points>
```

`<points>` is the number of points you earned for this game, with two decimals (see Scoring). Your program should exit after reading `GAME_END`.

## Output

Write exactly one line to standard output for each `ROUND`, then flush the output and wait for the next line. Don't print anything at any other time.

```
BID <amount>
```

The amount is a whole number from $0$ to your current cash.

## Scoring

What counts is how far ahead of your opponent you finish, not only whether you win. With $S = M \cdot (v_1 + v_2 + \ldots + v_K)$, the value of every good auctioned before bonuses, a game earns you

$5 + 10 \cdot \frac{\text{your total} - \text{opponent's total}}{S}$ 

points, but never less than $0$ or more than $10$. A tie earns $5$ points, and finishing ahead by half of $S$, or more, earns $10$.

A player that breaks the rules forfeits the game: 0 points for them, 10 for their opponent. Breaking the rules means bidding more than its cash, printing an invalid line, crashing, or going over the time or memory limit, which apply to each game separately.

Your score is proportional to the average of your points over the games.

## Example

The judge's messages for one game:

```
GAME 2 2 40 50 second
VALUES 10 20
ROUND 1 1 40 40
RESULT 1 9 9
ROUND 2 1 31 40
RESULT 1 12 12
ROUND 3 2 19 40
RESULT 0 20 19
ROUND 4 2 19 21
RESULT 0 15 11
GAME_END 1.50
```

Your program's answers, in order:

```
BID 12
BID 12
BID 19
BID 11
```

1. Two kinds of goods, each auctioned twice, $40$ cash each, a $50$ percent bonus and the second-price rule. You value good $1$ at $10$ and good $2$ at $20$; your opponent's values are a permutation of the same two numbers, and happen to be the same.
2. Good $1$ comes up. You bid $12$ against your opponent's $9$, so you take it and pay $9$, their bid.
3. Good $1$ again. Both bid $12$, the coin flip goes your way, and you pay $12$. You have now won every copy of good $1$, so with the bonus they are worth $10 \cdot 2 \cdot 1.5 = 30$ to you.
4. Good $2$ comes up. You bid all of your $19$ cash; your opponent bids $20$ and takes it for $19$.
5. Good $2$ again. Your $11$ loses to $15$, and your opponent takes it for $11$, completing their set of good $2$, worth $20 \cdot 2 \cdot 1.5 = 60$ to them.
6. You finish with $30$ in goods and $19$ cash, $49$ in all, against $60$ and $10$, $70$. With $S = 2 \cdot (10 + 20) = 60$, you earn $5 + 10 \cdot \frac{49 - 70}{60} = 1.5$ points.
