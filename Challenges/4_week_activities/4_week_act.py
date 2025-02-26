#-----------------------------------------------------------------------------
# Name:        Day-of-the-Week-Activity-Recommender
# Purpose:     recommending activities
# Author:      Sachin Vijay
# Created:     25-Feb-2025
# Updated:     25-Feb-2025
#---------------------------------------------------

# Adding a variable to  get input from the user, and to store it.
Day = input ("What day of the week is it? ")

# if anyone of the condition is not meet, the program will check other elif statements
# adding if statement to see if the entered day is monday or not
if Day == "Monday" or Day == "monday":
    print ('Start your week with a workout')

# adding elif statement to see if the entered day is tuesday or not
elif Day == "Tuesday" or Day == "Tuesday":
    print ("It's a great day to read a book")

# adding elif statement to see if the entered day is wednesday or not
elif Day == "Wednesday" or Day == "wednesday":
    print ("Mid-week movie night")

# adding elif statement to see if the entered day is thursday or not
elif Day == "Thursday" or Day == "Thursday":
    print ("Try new recipe")

# adding elif statement to see if the entered day is friday or not
elif Day == "Friday" or Day == "friday":
    print ('Relax and enjoy the weekend')

# adding elif statement to see if the entered day is saturday or not
elif Day == "Saturday" or Day == "Saturday":
    print ('Go for a hike')

# adding elif statement to see if the entered day is sunday or not
elif Day == "Sunday" or Day == "sunday":
    print ('Prepare for the week ahead with some self-care.')

else:
    print ( "Please enter a valid day")
