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

os.system("clear")
print(":::Welcome to the game:::")
player_name = input("Please enter your name: ")
print(f"Hello {player_name}, your dices are")
dice1 = randint(1,6)
dice2 = randint(1,6)
print(f"Dice 1: {dice1} Dice 2: {dice2}")

