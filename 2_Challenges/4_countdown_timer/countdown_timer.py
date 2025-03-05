#---------------------------------------------------
# Name:        Countdown timer
# Purpose:     to create countdown from 10 to 1 and asks user to stop
# Author:      Sachin Vijay
# Created:     4-Mar-2025
# Updated:     4-Mar-2025
#---------------------------------------------------
countdown = 10  # Initialize countdown before the loop
while countdown > 1:
    print(countdown)
    countdown -= 1  # Decrement countdown
    response = input("Should I stop?")
    if response == "yes":
        break
    else:
        continue