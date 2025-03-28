#---------------------------------------------------
# Name:        Tuple Basics
# Purpose:     To understand tuples
# Author:      Sachin
# Created:     28-Mar-2025
# Updated:     28-Mar-2025
# ---------------------------------------------------

#Create a tuple with float, integer, nested tuple and characters
tup = (22, 3.14, 'RRR', (1, 2, 3))

# print the tuple
print(tup, 'TUPLE')

# print the third item in the tuple
print(tup[2], 'third element of the tuple')

# extract and store the nested loop in a variable
nested = tup[3]

#print the first item of the nested loop using new variable
print(nested[0], 'first element of the nested tuple')