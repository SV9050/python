#-----------------------------------------------------------------------------
# Name:        Debug
# Purpose:     to find grades of students
# Author:      Sachin Vijay
# Created:     21-Feb-2025
# Updated:     24-Feb-2025
#---------------------------------------------------

# Adding a variable to  get input from the user, and to store it.

Name = input ('What is your Name?' )
Total_Marks = int(input ( 'What are total marks for this exam? '))

# string the percentage value in Percentage variable with its formulae
Percentage = float(Total_Marks / 100 * 100)

# adding if statement to see if the percentage is over 90
if Percentage >= 90 :
    print ('Your Grade is A and', Percentage, ' is your Percentage')

# adding elif statement to see if the percentage is between 80 and 90
elif Percentage >= 80:
        print('Your Grade is B', Percentage, ' is your Percentage')

# adding elif statement to see if the percentage is between 70 and 80
elif Percentage >= 70:
        print('Your Grade is C', Percentage, ' is your Percentage')

# adding elif statement to see if the percentage is over 60
elif Percentage >= 60:
    print('Your Grade is D', Percentage, ' is your Percentage')

 # adding else statement to see if the percentage is under 60
else:
        print('Your Grade is F', Percentage, ' is your Percentage')