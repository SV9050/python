# Initial grocery list
grocery_list = [' Apple ', 'Bread', 'Milk', 'Eggs']
response = input("Do you want to add any other items?: ")
if response == 'yes':

    user_input = input('Enter multiple fruits: ')

    fruits = user_input.split()

    grocery_list.extend(fruits)

    print("Updated grocery list:", grocery_list)

response_2 = input("Do you want to remove any items?: ")
if response_2 == 'yes':

    user_input_2 = input('Enter multiple fruits: ')

    removed_fruits = user_input_2.split()

    grocery_list.remove(removed_fruits)

    print("Removed fruits:", grocery_list)

else:
    print("Alright, no other items added.")
