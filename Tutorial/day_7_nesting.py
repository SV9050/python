#-----------------------------------------------------------------------------
# Name:        nesting
# Purpose:     adding another if statement with it
# Author:      Sachin Vijay
# Created:     12-Feb-2025
# Updated:     12-Feb-2025
#------------------------------------------------------

print ("Hello, Welcome to Indian Governemnt Portal")
Name = input ("What is your name?")
Citizenship = input ("Are you an Indian Citizen : ")
AadharCard = input ("Do you hold Aadhar card?")

# Need to add semicolon at the of if statement

if Citizenship == "Yes" and AadharCard == "Yes" :
    print ("Let us know if your income is under 12.75 lacs or not. If yes then enter '12.75 lacs'")
    Income = input ( "What is your annual income? :" )

# Adding another if statement
    if Income == "12.75 lacs" :
        print ("You are eligible for a complete rebate")
    else:
        print ("You are not eligible for a rebate")
        
# No identation for elif
        
elif Citizenship == "Resident":
    Income = input ( "What is your annual income? :" )
    print ("You are eligible for a rebate of 40k inr.")
else:
    print (Name, ", Sorry for the inconvience, but the service is only eligible for Indian Residents and Citizens")