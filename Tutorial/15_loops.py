#-----------------------------------------------------------------------------
# Name:       Loops
# Purpose:     To be able to loops
#
# Author:      Sachin Vijay
# Created:     27-Feb-2025
# Updated:     27-Feb-2025
#-----------------------------------------------------------------------------
Animal = input('What animal sound do you want to hear?: ')
while Animal == 'cow':  # Allow case-insensitive input
    print('Moo')
    exit = input('Do you want to stop? (yes/no): ')
    if exit == 'yes':
        break  # Exit the loop if the user wants to stop
    else:
        Animal = input('What animal sound do you want to hear?: ')# Ask again
        if Animal == 'Sheep':
            print('Baa')
print("Thank you for playing!")
