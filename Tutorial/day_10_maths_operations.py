#-----------------------------------------------------------------------------
# Name:        math operations
# Purpose:     using math operators 
# Author:      Sachin Vijay
# Created:     19-Feb-2025
# Updated:     19-Feb-2025
#---------------------------------------------------
print ( "Welcome to Profit Calculator")
Expenses = float(input(" What were your expenses this year?: "))
Revenue = float(input("What was your revenue this year?: "))
Profit = (Revenue - Expenses)
if Profit > 0 :
    print ("Great!!", "Your profit for current year is ,",Profit)
else:
    print ("loss")

