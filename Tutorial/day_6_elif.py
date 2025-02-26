#-----------------------------------------------------------------------------
# Name:        elif
# Purpose:     To make a basic elif program#
# Author:      Sachin Vijay
# Created:     12-Feb-2025
# Updated:     12-Feb-2025
#------------------------------------------------------

print ("Hello, Welcome to Indian Governemnt Portal")
Name = input ("What is your name?")
Citizenship = input ("Are you an Indian Citizen : ")

# Need to add semicolon at the of if statement

if Citizenship == "Yes" :
    print ("You are eligible for complete tax rebate")
        
# No identation for elif
        
elif Citizenship == "Resident":
    print ("You are eligible for a rebate of 40k inr.")
else:
    print (Name, ", Sorry for the inconvience, but this service is only valid for Indian Citizens")