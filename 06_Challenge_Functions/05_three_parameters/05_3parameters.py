#---------------------------------------------------
# Name:        3 Parameters
# Purpose:     to create a function that allows three parameters to be passed
# Author:      Sachin
# Created:     02-May-2025
# Updated:     02-May-2025
# ---------------------------------------------------

def tax(revenue, expense, unearned_revenue):
    payable = (revenue + unearned_revenue - expense) * 0.18
    print('Tax Payable is', payable)

tax(10000, 6000, 2000)





