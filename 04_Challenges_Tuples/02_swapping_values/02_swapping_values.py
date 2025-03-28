#---------------------------------------------------
# Name:        Swapping Values
# Purpose:     To swap values of the user in a tuple without third variable
# Author:      Sachin
# Created:     28-Mar-2025
# Updated:     28-Mar-2025
# ---------------------------------------------------

#Ask the user to input a number
user_1 = int(input('enter a value: '))

#Ask the user to input a number
user_2 = int(input('enter a value: '))

#Create a tuple with the users values
tup = (user_1, user_2)

#assign the user's input a reversed index values
user_2 = tup[0]
user_1 = tup[1]

#print

print('The swapped values are:',  user_1,  'and',  user_2 )
