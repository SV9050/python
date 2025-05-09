# Program Name: Sum of Numbers
# Purpose: This program takes a number 'n' from the user and calculates the sum of all numbers from 1_Updating_List to 'n' using a for loop.
# Creator: Rohan Singh
# Student Number: 931006
# Date: March 6, 2025

# We will ask the user for a number 'n' and then calculate the sum of all numbers from 1_Updating_List to 'n'.

# Step 1_Updating_List: Ask the user to enter a number
print("Welcome to the Sum of Numbers program!")
n = int(input(
    "Please enter a positive integer 'n' to calculate the sum of all numbers from 1_Updating_List to 'n': "))  # Convert input to an integer

# Step 2: Check if the number is valid
if n <= 0:
    print("Sorry, the number must be greater than 0. Please restart the program and enter a valid number.")
else:
    # Step 3: Initialize a variable to store the sum
    sum_of_numbers = 0  # This variable will store the sum of numbers

    print(f"\nLet's calculate the sum of all numbers from 1_Updating_List to {n}.")

    # Step 4: Use a for loop to add numbers from 1_Updating_List to 'n'
    for i in range(1, n + 1):  # Loop from 1_Updating_List to n
        sum_of_numbers += i  # Add the current number to the sum
        print(f"Adding {i}: Current sum is {sum_of_numbers}")  # Show the current step

    # Step 5: Display the result
    print(f"\nThe total sum of all numbers from 1_Updating_List to {n} is {sum_of_numbers}.")  # Output the final sum