#---------------------------------------------------
# Name:        Guess the number
# Purpose:     to guess the number using while loop
# Author:      Sachin Vijay
# Created:     4-Mar-2025
# Updated:     4-Mar-2025
#---------------------------------------------------

import random

# Generate a random number between 1 and 10
Random_Number = random.randint(1, 10)

# Start the guessing loop
while True :
    # Ask the user to guess the number
    guess = int(input("Guess a number between 1 and 10: "))

    # Check if the guess is correct
    if guess == Random_Number:
        print("Congratulations! You guessed it correctly, the number is", Random_Number)
        break  # Exit the loop if the guess is correct
    else:
        print("Incorrect guess. Try again!")
