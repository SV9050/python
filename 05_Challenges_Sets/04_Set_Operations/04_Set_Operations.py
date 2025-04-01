#---------------------------------------------------
# Name:        Set Operations
# Purpose:     Performing set operations like union, intersection, and difference.
# Author:      Sachin
# Created:     01-Apr-2025
# Updated:     01-Apr-2025
# ---------------------------------------------------

# Define two sets of numbers
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}


# Update set1 to keep only the numbers that are in both sets (intersection)
set1.intersection_update(set2)

# Print the intersection of set1 and set2
print('Intersection:', set1)


# Perform union of set1 and set2 but do not change set1
set1.union(set2)

# Print set1, which has not changed
print('Union:', set1)


# Update set1 to remove numbers that are in set2 (difference)
set1.difference_update(set2)

# Print the updated set1 after removing elements from set2
print('Difference:', set1)

