#-----------------------------------------------------------------------------
# Name:       if / else 
# Purpose:     To be able to use if and else statement
#
# Author:      Sachin Vijay
# Created:     10-Feb-2025
# Updated:     10-Feb-2025
#-----------------------------------------------------------------------------

print ("Hello, Welcome to Indian Governemnt Portal")
Name = input ("What is your name?")
Citizenship = input ("Are you an Indian Citizen : ")

# Need to add semicolon at the of if statement

if Citizenship == "Yes" :
    print ("Let us know if your income is under 12.75 lacs or not. If yes then enter '12.75 lacs'")
    Income = input ( "What is your annual income? :" )
    
# I added another if statement for incomes level under 12.75 looking for rebate

    
    if Income == ("12.75 lacs") :
        print ("Congrats",Name,"As your income",Income, "is under 12.75 lac per year, you are eligible for tax rebate, Kindly Check the webiste for details")
    else :
        print ("Sorry",Name,", As your income",Income, "is above 12.75 lac per year, you are not eligible for any tax rebate, Kindly Check the webiste for details")
elif Citizenship == "Resident" :
    print ("gube")
#This this the else statement for the first if statement, this syas that they are eligible

else :
    print (Name, ", Sorry for the inconvience, but this service is only valid for Indian Citizens")
    