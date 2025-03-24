#---------------------------------------------------
# Name:        removing Lists
# Purpose:     removing the list based on user's input
# Author:      Sachin Vijay
# Created:     18-Mar-2025
# Updated:     18-Mar-2025
# ---------------------------------------------------

todo_list = ['write email', 'finish homework', 'call mom', 'clean room']
print ( todo_list )
remo_1 = input('What should be removed form the list: ')
if remo_1 == 'call mom':
    todo_list.remove(remo_1)
    print ( 'New List', todo_list)
else:
    print('call your mom')
remo_2 = input('Its been a while, What should be removed?: ')
if remo_2 == 'clean room':
    todo_list.remove(remo_2)
    print ( 'New List', todo_list)
else:
    print('clean your room now')
