#---------------------------------------------------
# Name:        Functions with 2 Parameters
# Purpose:     To create functions that allows two parameters to be passed
# Author:      Sachin
# Created:     01-May-2025
# Updated:     01-May-2025
# ---------------------------------------------------

num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))
def addi(a,b):
    result = a+b
    print (' The result of', a, 'and', b, 'is', result)
# Call the function
addi(num_1,num_2)
