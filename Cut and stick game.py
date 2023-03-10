#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def play():
    user_option = input("'r for rock:', 'p for paper:', or 's for scissors: or q to quit':")
    cpu = random.choice(['r', 's', 'p'])
    #while user_option != 'y':

    if user_option == cpu:
        return("You tie!")
    if win(user_option, cpu):
        return("You won!")

    return "You lost!"
  
def win(player, computerOpponent):
    if (player == 'r' and computerOpponent == 's') or (player == 's' and computerOpponent == 'p') or (player == 'p' and computerOpponent == 'r'):
        return True

print(play())  


# In[ ]:




