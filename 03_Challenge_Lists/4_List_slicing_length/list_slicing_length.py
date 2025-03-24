#---------------------------------------------------
# Name:       Slicing items on list using index
# Purpose:     Modifying an existing item in a list
# Author:      Sachin Vijay
# Created:     19-Mar-2025
# Updated:     19-Mar-2025
# ---------------------------------------------------

# Creating colors list
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print (colors)

# slicing/extracting items from the list using their index and storing it in a variable
two = colors[1:3]

# deleting the items from the list using del function
del colors[1:3]

# printing the stored variable
print('Extracted', two, 'colors')

# printing the length of updated list
print ('The list contains',len(colors), 'items')

# printing the updated list
print('updated list', colors)