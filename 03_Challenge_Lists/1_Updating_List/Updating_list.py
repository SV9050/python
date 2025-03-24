#---------------------------------------------------
# Name:        Updating Lists
# Purpose:     Updating the list based on user's input
# Author:      Sachin
# Created:     18-Mar-2025
# Updated:     18-Mar-2025
# ---------------------------------------------------

# Creating a grocery list
grocery_list = [' Apple ', 'Bread' , 'Milk' , 'Eggs']

# Asking the user to enter a fruit and a dairy product
fruit_1 = input('Enter a Fruit: ').lower()
fruit_2 = input('Enter a Dairy Product: ').lower()

# Adding if statement to check if the entered items are according to the question
if fruit_1 == 'tomatoes' and fruit_2 == 'cheese':

    # if yes, the fruit entered will be added to the list in the index 0
    grocery_list.insert(0,fruit_1)

    # will append the dairy product
    grocery_list.append(fruit_2)

    # Print the updated list
    print(grocery_list)

else:
    print('Please try again')