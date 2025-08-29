# 🎲 Dice Rolling Game & Ranker

A non-interactive command-line script that simulates a dice game where four players each roll a six-sided die. The script then displays the results and a final ranking from highest to lowest roll.

## Features

* **Game Simulation**: Automatically simulates a dice roll (1-6) for four automated players.
* **Result Ranking**: Sorts the players based on their dice roll in descending order to create a leaderboard.
* **Clear Output**: First shows the individual rolls as they happen (with a 1-second delay), then displays the final ranked list.
* **Efficient Sorting**: Uses `operator.itemgetter` for efficient sorting of the results dictionary.

## How to Use

1.  Ensure you have Python installed.
2.  Save the code as a `.py` file (e.g., `dice.py`).
3.  Run the script from your terminal:
    ```sh
    python dice.py
    ```
4.  The script will run automatically, showing each player's roll and then the final ranking.

### Example Output

```sh
> python dice.py
------Dice Rolling------
The Player 1 rolled 4 on the dice
The Player 2 rolled 6 on the dice
The Player 3 rolled 2 on the dice
The Player 4 rolled 4 on the dice
------Ranking------
Player 2: 6
Player 1: 4
Player 4: 4
Player 3: 2
```
