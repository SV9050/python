#---------------------------------------------------
# Name:        Set Methods
# Purpose:     Using set methods like `.copy()`, `.clear()`, and `.pop()`.
# Author:      Sachin
# Created:     01-Apr-2025
# Updated:     01-Apr-2025
# ---------------------------------------------------

# Define a set of numbers
data = {10, 20, 30, 40, 50}

# Create a copy of the original set
data_copy = data.copy()

# Print the copied set
print('Copy:', data_copy)

# Remove and return an arbitrary element from the set
data.pop()

# Print the set after removing one element
print('After Pop:', data)

# Remove all elements from the set
data.clear()

# Print the set after it has been cleared
print('After Clear:', data)