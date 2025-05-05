

STEP 1: CREATE FUNCTION
        FUNCTION tax(revenue, expense, unearned_revenue)

Step 2: FIND THE PAYABLE TAX
    total_revenue = revenue + unearned_revenue
    taxable_income = total_revenue - expense
    payable = taxable_income * 0.18
    RETURN payable
    END FUNCTION

STEP 3: PRINT THE PAYABLE TAX
        PRINT "Tax Payable is", payable


payable_tax = CALL tax(10000, 6000, 2000)


