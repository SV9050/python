#---------------------------------------------------
# Name:        True or Else
# Purpose:     to check if a variable is even number
# Author:      Sachin
# Created:     30-Apr-2025
# Updated:     30-Apr-2025
# ---------------------------------------------------

def tax(revenue, expense, unearned_revenue):
    payable = (revenue + unearned_revenue - expense) * 0.18
    print('Tax Payable is', payable)

tax(10000, 6000, 2000)





