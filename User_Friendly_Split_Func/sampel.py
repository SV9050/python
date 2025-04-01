# Initial grocery list
grocery_list = [' Apple ', 'Banana', 'Dragan Fruit', 'Durian']
print("Hello, this is your current grocery list:", grocery_list)
response = input("Do you want to add any other fruits?: yes or no: ").lower()
if response == 'yes':

    user_input = input('Enter multiple fruits: ')

    fruits = user_input.split()

    grocery_list.extend(fruits)

    print("Updated grocery list:", grocery_list)

else:
    print("Alright, no other items added.")
