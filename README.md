# Hangman Game

Welcome to the Hangman Game! This is a simple command-line implementation of the classic Hangman game, where you have to guess a hidden word by suggesting letters within a certain number of attempts.

## How to Play

1. **Start the Game**: When you run the script, you will be welcomed to the Hangman game.
2. **Set Attempts**: You will be prompted to enter the number of attempts you want. Make sure to enter a numeric value.
3. **Hints**: The game will provide a hint related to the hidden word.
4. **Guessing Letters**: Enter letters one by one to guess the hidden word. If the letter is in the word, it will be revealed in its correct positions. If not, you will lose an attempt.
5. **Winning and Losing**: The game ends when you either guess the word correctly (win) or run out of attempts (lose).

## Code Overview

### Dependencies

The game only requires Python's built-in modules: `random` and `sys`.

### Files

- `hangman.py`: The main script to run the Hangman game.

### Code Breakdown

1. **Initialize the Game**:

   - Greet the player.
   - Prompt the player to enter the number of attempts.

2. **Input Validation**:

   - Ensure the number of attempts is a numeric value.

3. **Word Selection and Hint**:

   - A random word is selected from a predefined list.
   - A corresponding hint is displayed.

4. **Game Mechanics**:

   - Display the current state of the word with underscores for unguessed letters.
   - Allow the player to guess letters.
   - Update the display based on correct or incorrect guesses.
   - Track the number of attempts left.

5. **Hangman Drawing**:

   - Visual representation of the hangman based on the number of incorrect guesses.

6. **End of Game**:
   - Congratulate the player if the word is guessed correctly.
   - Inform the player if they run out of attempts.

### Functions

- `hangman(n, m)`: Draws the hangman based on the number of incorrect guesses (`n`) and remaining attempts (`m`).
- `lenOfNewList(newList)`: Counts the number of correctly guessed letters in the current state of the word.

### Example Run

```plaintext
Welcome to Hangman
Enter the Number of Attempt : 5
Hint : fruit
Enter a Letter ( Enter 'QUIT' to exit ) : a
Word :
a____
Good Guess
__________
```

## Requirements

- Python 3.x

## How to Run

1. Ensure you have Python 3 installed on your system.
2. Download or copy the `hangman.py` file.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `hangman.py`.
5. Run the script with the command:

```bash
python hangman.py
```

## Author

This project was created as part of a test for 7EDGE.

---

Enjoy the game and happy guessing!
