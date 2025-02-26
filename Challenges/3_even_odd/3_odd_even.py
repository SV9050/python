#-----------------------------------------------------------------------------
# Name:        to find if an number is odd or even
# Purpose:     to learn how to use remainder function and conditionals
# Author:      Sachin Vijay
# Created:     24-Feb-2025
# Updated:     24-Feb-2025
#---------------------------------------------------

#Adding a variable to  get input from the user, and to store it.
number = float(input('Enter a number: '))

#Adding if statement to see if the variable has remainder as 0 when it is divided by 2, if yes then it is an even number
if number % 2 == 0:
    print (number,'is an even number')

#Else it'll be an odd number
else:
    print (number,'is an odd number')