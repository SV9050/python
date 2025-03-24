#---------------------------------------------------
# Name:        Sum of N
# Purpose:     To find the sum of first N numbers using a for loop
# Author:      Sachin Vijay
# Created:     4-Mar-2025
# Updated:     4-Mar-2025
# ---------------------------------------------------

# Ask the user to enter a number N
N = int(input("Enter a number: "))

# Set a variable to store the total sum
total = 0

# Iterate till N (inclusive) and calculate the sum
for added_value in range(N+1):

    # Add the current value to the total
    total += added_value


# Print the final sum
print(total)