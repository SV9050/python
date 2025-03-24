# ---------------------------------------------------
# Name:        Skip Even Numbers
# Purpose:     Demonstrate skipping even numbers using `continue`
#              in a `for` loop and only printing odd numbers.
# Author:      Sachin Vijay
# Created:     4-Mar-2025
# Updated:     4-Mar-2025
# ---------------------------------------------------

# Loop through numbers 1_Updating_List to 10
for n in range(1, 11):
    # Check if the number is even
    if n % 2 == 0:

        continue
    # If the number is not even, print it
    print(n)