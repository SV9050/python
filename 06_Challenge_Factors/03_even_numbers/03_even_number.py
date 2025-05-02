#---------------------------------------------------
# Name:        True or Else
# Purpose:     to check if a variable is even number
# Author:      Sachin
# Created:     30-Apr-2025
# Updated:     30-Apr-2025
# ---------------------------------------------------

def is_even(number):
    return number % 2 == 0

#  user input
user_input = int(input("Enter a number: "))

print(is_even(user_input))


