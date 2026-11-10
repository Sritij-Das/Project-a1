
import random

def number_guessing_game():
    print("Welcome to the game!\n")

    max_num = int(input("The maximum number you could guess?\n"))
    print("\nWell, so I have decided...\n")

    while True:
        try:
            max_attempts = int(input("How many attempts would you like?\n"))

            if 0 < max_attempts < max_num:
                break

            print(f"Please enter a number greater than 0 and less than {max_num}.")

        except ValueError:
            print("Invalid input, please enter a whole number.")

    random_number = random.randint(1, max_num)
    attempts = 0

    while attempts < max_attempts:
        remaining_attempts = max_attempts - attempts
        print(f"\nYou have {remaining_attempts} attempts left.")

        try:
            guess = int(input("Enter your guess: "))

        except ValueError:
            print("Invalid input! Enter a valid number.")
            continue

        attempts += 1

        if guess == random_number:
            print(f"You found {random_number} in {attempts} attempts!")
            return

        elif guess < random_number:
            print("Too low! Try a higher number.")

        else:
            print("Too high! Try a lower number.")

    print(f"Game Over! You ran out of attempts. The number was {random_number}.")

# Run
number_guessing_game()
