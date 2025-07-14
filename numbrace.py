'''
crear un juego de numeros con las siguientes condiciones

solicitar cantidad de jugadores (min 2 max 4)

solicitar el nivel del juego
basico 20 posiciones
intermedio 30 posiciones
avanzado 50 posiciones
experto 100 posiciones

cada jugar tiene un turno de lanzamiento de dos dados hasta que el primer jugador llegue al final se termina el juego

si el jugador obtiene 3 pares consecutivos gada la partida
'''
#### imports ####
import os
from random import randint
import time
from tqdm import tqdm

os.system("clear")

#### functions ####
def roll_dices():
    d1 = randint(1,6)
    d2 = randint(1,6)
    return d1, d2

def valid_players(x, y):
    while True:
        usrInput = int(input(x))
        if usrInput in y:
            return usrInput
        else:
            print("Please enter a valid option")

def create_players(x):    
    for i in range(x):
        players[f"player_{i + 1}"] = 0
    return players

def set_difficulty(x,y):
    while True:
        usrInput = int(input(x))
        if usrInput in y:
            if usrInput == 1:
                goal = 20
            elif usrInput == 2:
                goal = 30
            elif usrInput == 3:
                goal = 50
            elif usrInput == 4:
                goal = 100
        return goal

def progress_bar(x):
    for _ in tqdm(range(x),desc="Loading positions",unit="s"):
        time.sleep(0.06)

def print_player(x):
    return "\n".join([f"{key}\t{value}" for key, value in x.items()])
    


#### main ####

players = {}

print(".::: Numerical Race :::.")
nplayers = valid_players("Multiplayer(2-4)\nEnter the number of players: ",[2,3,4])
create_players(nplayers)

os.system("clear")

difficultyPrompt='''.::: Numerical Race :::.
set game difficulty:

[1]  Basic:         (20 positions)
[2]  Intermediate:  (30 positions)
[3]  Advanced:      (50 positions)
[4]  Expert:        (100 positions)

enter your option (1-4): '''

levels = set_difficulty(difficultyPrompt,[1,2,3,4])

progress_bar(levels)
input("Everything ready. Press enter to start game")
os.system("clear")

displayPrompt=f'''.::: Numerical Race :::.
Game difficulty: {levels} positions.
Players      Position
{print_player(players)}
'''
print(displayPrompt)
while True:
    finish = [player for player, value in players.items() if value >= levels]
    if finish:
        print(f"{'y'.join(finish)} is the winner")
        break

    for player in players:
        if players[player] < levels:
            d1, d2 = roll_dices() 
            progres = d1 + d2
            players[player] += progres
            print(f"Dice 1: {d1}\nDice 2: {d2}")
            input("Press enter to next player")
            os.system("clear")
            print(displayPrompt)
        
    print(displayPrompt)
    print(players)
        
