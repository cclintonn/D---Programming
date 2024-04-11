# Midunit 2 Activity
# Author: Clinton Chieng
# 11 April 2024

import random
def guess_number():
    number_to_guess = random.randint(1, 100)
    guess = 0
    attempts = 0

    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again. ")
        elif guess > number_to_guess:
            print("Too high! Try again. ")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

guess_number()