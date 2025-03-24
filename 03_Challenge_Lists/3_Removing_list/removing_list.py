#---------------------------------------------------
# Name:        removing Lists
# Purpose:     removing the list based on user's input
# Author:      Sachin Vijay
# Created:     18-Mar-2025
# Updated:     18-Mar-2025
# ---------------------------------------------------


# Creating a to do list
todo_list = ['write email', 'finish homework', 'call mom', 'clean room']

# Print the initial list
print ( todo_list )

# asking the user to remove an item from the list
remo_1 = input('What should be removed form the list: ')

# using the if statement to check the if input is matching the questions requirement
if remo_1 == 'call mom':

    # using .remove operation to remove the entered item from the list
    todo_list.remove(remo_1)

    # printing new list
    print ( 'New List', todo_list)


else:
    print('call your mom')

# asking the user to remove another item from the list
remo_2 = input('Its been a while, What should be removed?: ')

# using the if statement again to check if the input is matching the questions requirement
if remo_2 == 'clean room':

    # using .remove operation to remove the 2nd  item from the list
    todo_list.remove(remo_2)
    print ( 'New List', todo_list)

else:
    print('clean your room now')
