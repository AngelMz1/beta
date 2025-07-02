'''
description:
get name player
generate two random numbers into 2 dices
dice 1: 1-6
dice 2: 1-6
print dices value
if dice 1 and dice 2 is pair print YOU WIN else print YOU LOSE
'''
import os
from random import randint
#####################################
#functions
#####################################

def get_dices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1, dice2
def get_result(x, y):
    if x % 2 == 0  and y % 2 == 0:
        result = "YOU WIN"
    else:
        result = "YOU LOSE"
    return result
os.system("clear")

print("::: Welcome to the game :::")
print(f"Hello your dices are")

dice1, dice2 = get_dices()
result = get_result(dice1, dice2)


print(f"Dice 1: {dice1} Dice 2: {dice2}")
print(result)