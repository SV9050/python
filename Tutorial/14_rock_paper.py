#-----------------------------------------------------------------------------
# Name:       Rock Paper Scissor
# Purpose:     To be able to use if and else statement and create a game
#
# Author:      Sachin Vijay
# Created:     27-Feb-2025
# Updated:     27-Feb-2025
#-----------------------------------------------------------------------------
print ("Welcome to Rock, Paper, Scissors!", " Enter R for rock, P for paper, S for scissors")
Player_1 = input(" Player 1 : Rock, Paper or Scissors? ")
Player_2 = input(" Player 2 : Rock, Paper or Scissors? ")
if Player_1 == 'R' and Player_2 == 'P':
    print ("Player 2 wins!")
elif Player_1 == 'R' and Player_2 == 'S':
    print ("Player 1 wins!")
elif Player_1 == 'P' and Player_2 == 'R':
    print ("Player 1 wins!")
elif Player_1 == 'P' and Player_2 == 'S':
    print ("Player 2 wins!")
elif Player_1 == 'S' and Player_2 == 'R':
    print ("Player 2 wins!")
elif Player_1 == 'S' and Player_2 == 'P':
    print ("Player 1 wins!")
elif Player_1 == Player_2:
    print ("It's a tie!")
else:
    print ("Invalid input!")