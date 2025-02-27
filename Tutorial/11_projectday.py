#-----------------------------------------------------------------------------
# Name:        Project day
# Purpose:     to find seconds
# Author:      Sachin Vijay
# Created:     19-Feb-2025
# Updated:     21-Feb-2025
#---------------------------------------------------
# Making to input values
Seconds = float(input("How many Seconds in a minute ? "))
Minutes = float(input("minutes in a hour "))
qHours = float(input(" number of hours in a day? "))
Days = int(input(" How many Days in an year? "))
# Adding the formulas to two variables
secondsinhours = (Seconds * Minutes) # this is 60*60 = 3600
SecondsInADay =  (secondsinhours * qHours) # this is 3600 * 24 = 86400
# adding conditional statement
if Days == 365 :
    print (SecondsInADay * Days) # this is 86400*365 = 31536000
elif Days == 366 :
    print  (SecondsInADay * Days)
else:
 print ("Please enter an correct value")