#---------------------------------------------------
# Name:        Tuple operation and count
# Purpose:     to know how many times a fruit appears in the tuple.
# Author:      Sachin
# Created:     28-Mar-2025
# Updated:     28-Mar-2025
# ---------------------------------------------------

# Step 1: Create a tuple with repeated values
fruits = ("apple", "banana", "apple", "cherry", "banana", "apple")


# Step 2: Ask the user to enter a fruit name
user_fruit = input('Enter a fruit name: ')


# Step 3: Count how many times the fruit appears in the tuple
count = fruits.count(user_fruit)


# Print the result
print(f"'{user_fruit}' appears {count} times in the tuple.")