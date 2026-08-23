# Python Pig Dice Game

A command-line multiplayer Pig Dice game built with Python. Players take turns rolling a dice and try to reach the target score before their opponents.

## Features

- Supports 2–4 players
- Random dice rolls from 1 to 6
- Player score tracking
- Turn-based gameplay
- Score reset when a player rolls a 1
- Input validation for the number of players
- Winner detection
- Target score of 50 points

## How It Works

Players first choose how many people will play. The game supports between 2 and 4 players.

Each player takes a turn and can choose whether to roll the dice.

If the player rolls a number from 2 to 6, that number is added to their current turn score.

If the player rolls a 1, their turn ends and their accumulated score for that turn is lost.

At the end of the turn, the accumulated score is added to the player's total score.

The game continues until a player reaches the target score.

## Rules

- Players must be between 2 and 4.
- The dice produces a random number from 1 to 6.
- Rolling 1 ends the current turn and loses the points accumulated during that turn.
- Rolling 2–6 adds the number to the current turn score.
- The first player to reach 50 points wins.

## Example

```text
How many players (2-4): 3

Player No 1 its your turn.
Your current score is 0

Do you want to roll the dice (y/n): y
You rolled a 5
Your score is 5

Do you want to roll the dice (y/n): n
Your total score is 5
