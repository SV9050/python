#---------------------------------------------------
# Name:        Updating Lists
# Purpose:     Updating the list based on user's input
# Author:      Sachin
# Created:     18-Mar-2025
# Updated:     18-Mar-2025
# ---------------------------------------------------

grocery_list = [' Apple ', 'Bread' , 'Milk' , 'Eggs']
fruit_1 = input('Enter a Fruit: ')  # Prompt updated for clarity
fruit_2 = input('Enter a Dairy Product: ')

if fruit_1 == 'Tomatoes' or 'tomatoes' and fruit_2 == 'Cheese' or 'cheese':

    grocery_list.insert(0,fruit_1)  # Correctly use the insert method
    grocery_list.insert(5, fruit_2)
    print(grocery_list)  # Print the updated list
else:
    print('Please try again')