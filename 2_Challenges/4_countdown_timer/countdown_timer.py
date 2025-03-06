#---------------------------------------------------
# Name:        Countdown timer
# Purpose:     to create countdown from 10 to 1 and asks user to stop
# Author:      Sachin Vijay
# Created:     4-Mar-2025
# Updated:     4-Mar-2025
#---------------------------------------------------
countdown = 10
while countdown > 0:
    print(countdown)
    response = input("Should I stop?")
    countdown -= 1  # Decrement countdown
    if response == "yes":
        break
    else:
        continue