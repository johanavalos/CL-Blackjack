# CL-Blackjack

This is an implementation of the game Blackjack in python in the command line.

## Blackjack Rules

### Objective
The goal of Blackjack is to beat the dealer by having a hand value as close to 21 as possible without exceeding it.

### Card Values
- Number cards (2-10) are worth their face value.
- Face cards (Jack, Queen, King) are worth 10 points each.
- Aces can be worth either 1 or 11 points, depending on what benefits the player’s hand.

### Setup
- The game is typically played with one or more decks of standard 52-card playing cards.
- Each player places a bet before the round starts.
- The dealer gives two cards to each player and two to themselves. One of the dealer’s cards is face-up (the "upcard"), and the other is face-down (the "hole card").

### Player Actions
Players can take the following actions on their turn:
- **Hit**: Take another card to increase the hand value.
- **Stand**: Keep the current hand and end the turn.
- **Double Down**: Double the initial bet and receive only one more card.
- **Split**: If the first two cards are of the same rank, the player can split them into two separate hands, placing an additional bet equal to the original bet.
- **Surrender** (if allowed): Forfeit the hand and recover half the original bet.

### Dealer Rules
- The dealer must hit if their hand totals 16 or less.
- The dealer must stand if their hand totals 17 or higher (some casinos require the dealer to hit on a "soft 17," which is a hand containing an Ace valued as 11).

### Winning and Payouts
- **Blackjack**: A two-card hand totaling 21 (Ace + 10-value card) pays 3:2.
- **Win**: A player’s hand value is higher than the dealer’s without exceeding 21, paying 1:1.
- **Push**: A tie between the player and dealer results in no win or loss.
- **Bust**: If a hand exceeds 21, the player loses immediately.

### Additional Rules
- Insurance: If the dealer's upcard is an Ace, players can make an additional bet (up to half the original bet) that pays 2:1 if the dealer has Blackjack.
- Even Money: If the player has a Blackjack and the dealer's upcard is an Ace, the player can take an "even money" payout instead of risking a push.

## User Manual

Run `python main.py` followed by the usernames separated by spaces. For example, if Pablo and Lucía want to play, the command would be the following:
```
    python main.py Pablo Lucía
```

## Credits

- Johan Ávalos
