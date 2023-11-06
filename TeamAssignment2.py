#Enxhi Merkaj 11/5/2023
#Team Assignment

#Python program that allows the user to guess a randomly generated number
# and continues looping until the user chooses to stop

import random

def main():
    while True:
        play_game()
        play_again = input("Would you like to guess another number (Y/N)? ").strip().lower()
        if play_again != 'y':
            break

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I've selected a random number between 1 and 100.")

    while True:
        guess = input("Please enter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Try guessing higher.")
        elif guess > secret_number:
            print("Try guessing lower.")
        else:
            print(f"Congratulations! You've guessed the number ({secret_number}) in {attempts} attempts.")
            break

if __name__ == "__main__":
    main()
