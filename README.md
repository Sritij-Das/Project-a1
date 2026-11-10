# 🎮 Number Guessing Game (Python)

A simple and interactive command-line Number Guessing Game built using Python. The computer randomly selects a number, and the player has to guess it within a limited number of attempts.

The game provides hints after every guess, helping the player figure out whether the guessed number is too high or too low.

## 📌 Features

- **Random Number Generation:** Computer randomly selects a number using Python's `random` module.
- **Custom Number Range:** Players can decide the maximum number for the guessing range.
- **Limited Attempts:** Players can set their own attempt limit.
- **Instant Feedback:** Get hints such as "Too High" or "Too Low" after every guess.
- **Input Validation:** Handles invalid inputs using exception handling.
- **Attempt Tracking:** Displays the remaining attempts after each guess.
- **Win/Lose Conditions:** Announces whether the player wins or runs out of attempts.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Modules:** `random`
- **Concepts Used:**
  - Functions
  - While Loops
  - Conditional Statements
  - User Input (`input()`)
  - Type Conversion
  - Exception Handling (`try-except`)
  - Random Number Generation

## 🚀 How to Run the Project

**1. Clone the repository**

```bash
git clone https://github.com/Sritij-Das/number-guessing-game.git
```

**2. Navigate to the project directory**

```bash
cd number-guessing-game
```

**3. Run the Python file**

```bash
python number_guessing_game.py
```

## 🎯 How to Play

1. Enter the maximum number for the guessing range.
2. Choose how many attempts you want.
3. Start guessing the randomly generated number.
4. Follow the hints:
   - Too Low → Guess a higher number.
   - Too High → Guess a lower number.
5. Find the correct number before running out of attempts!

## 💻 Sample Output

```text
Welcome to the game!

The maximum number you could guess?
50

Well, so I have decided...

How many attempts would you like?
5

You have 5 attempts left.
Enter your guess: 25
Too low! Try a higher number.

You have 4 attempts left.
Enter your guess: 35
Too high! Try a lower number.

You have 3 attempts left.
Enter your guess: 30
You found 30 in 3 attempts!
```

## 📚 What I Learned

Through this project, I practised:

- Writing and calling Python functions.
- Implementing loops and conditional logic.
- Generating random numbers.
- Handling invalid user inputs.
- Managing attempts using variables.
- Building an interactive command-line application.

## 🔮 Future Improvements

- Add difficulty levels (Easy, Medium, Hard).
- Allow players to restart the game.
- Add a scoring system.
- Track the player's best score.

## 👨‍💻 Author

**Sritij Das**
---
⭐ If you like this project, feel free to star the repository!
