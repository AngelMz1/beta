'''
description:
get name player
generate two random numbers into 2 dices
dice 1: 1-6
dice 2: 1-6
print dices value
'''
import os
from random import randint
#####################################
#functions
#####################################
print(":::Welcome to the game:::")
os.system("clear")
player_name = input("Please enter your name: ")
print(f"Hello {player_name}, your dices are")
def get_dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    print(f"Dice 1: {dice1} Dice 2: {dice2}")
get_dices()