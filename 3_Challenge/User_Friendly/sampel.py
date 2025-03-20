# Initial grocery list
grocery_list = [' Apple ', 'Bread', 'Milk', 'Eggs']


user_input = input('Enter multiple fruits: ')

fruits = user_input.split()

grocery_list.extend(fruits)

print("Updated grocery list:", grocery_list)
