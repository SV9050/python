#---------------------------------------------------
# Name:        Sum of N
# Purpose:     to find sum of n using for loop
# Author:      Sachin Vijay
# Created:     4-Mar-2025
# Updated:     4-Mar-2025
#---------------------------------------------------
N = int(input("Enter a number: "))
total = 0
for added_value in range(N+1):
    total += added_value
print(total)