#---------------------------------------------------
# Name:        Countdown timer
# Purpose:     to create countdown from 10 to 1_Updating_List and asks user to stop
# Author:      Sachin Vijay
# Created:     4-Mar-2025
# Updated:     4-Mar-2025
#---------------------------------------------------
# Set the countdown value
countdown = 10

# Start a loop that continues as long as the countdown is greater than 0
while countdown > 0:
    # Print the current countdown value
    print(countdown)

    # Ask the user if the countdown should stop
    response = input("Should I stop?")

    # Decrease the countdown value by 1_Updating_List
    countdown -= 1  # Decrement countdown

    # If the user responds
    # "yes", exit the loop
    if response == "yes":
        print("Boom")
        break

    # Otherwise, continue the loop
    else:
        continue