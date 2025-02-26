#-----------------------------------------------------------------------------
# Name:        to find weather
# Purpose:     finding weather and warning
# Author:      Sachin Vijay
# Created:     24-Feb-2025
# Updated:     24-Feb-2025
#---------------------------------------------------

# Adding a variable to  get input from the user, and to store it.
Name = input ('What is your Name?' )
Weather = float(input ( 'Please enter temperature in celsius '))

# adding if statement to see if the entered temperature is under 18
if Weather <= 10 :
    print ('Its cold outside. Wear a jacket!')

# adding elif statement to see if the entered temperature is between 10 & 25
elif Weather <= 25:
        print('its a nice day. Wear short-sleeves!')

# adding else statement to see if the entered temperature is over 25
else:
        print('Its hot outside. Stay cool!')