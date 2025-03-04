#-----------------------------------------------------------------------------
# Name:        Voting-Eligibility-Checker
# Purpose:     checking age for vote eligibility
# Author:      Sachin Vijay
# Created:     25-Feb-2025
# Updated:     25-Feb-2025
#--------------------------------------------------

# Adding a variable to  get input from the user, and to store it.
Name= input ('Hello, What is your name?: ')
Age= int(input ('What is your age?: '))

# adding if statement to see if the entered age is above 18
if Age >= 18:
    print ("You are eligible to vote!")

# adding else statement to see if the entered age is below 18
else:
    print ("You are not eligible to vote!")