#-----------------------------------------------------------------------------
# Name:        project
# Purpose:     adding conditions
# Author:      Sachin Vijay
# Created:     12-Feb-2025
# Updated:     12-Feb-2025
#------------------------------------------------------

print("Welcome to the UI test")
Name = input (" What is your name? : ")
Movie = input ( "Did you watch Upendra's UI? : ")
if Movie == "Yes" or "yes":
    Rating = int(input("On a scale of 1_Updating_List - 10 how do you like the movie? : "))
    if Rating > 7 :
        print ( "Super ra bittu, this is the best timing ever")
    else:
        print (" Gube, get concentration and focus ra")
else:
    print ("Watch the movie")