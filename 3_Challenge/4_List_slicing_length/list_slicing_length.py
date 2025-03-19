#---------------------------------------------------
# Name:       Slicing items on list using index
# Purpose:     Modifying an existing item in a list
# Author:      Sachin Vijay
# Created:     19-Mar-2025
# Updated:     19-Mar-2025
# ---------------------------------------------------

colors = ['red', 'blue', 'green', 'yellow', 'purple']
two = colors[1:3]
del colors[1:3]
print(two)
print (len(colors))
print(colors)