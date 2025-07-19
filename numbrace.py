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
        usrInput = input(x)
        if usrInput.isdigit():
            numInput = int(usrInput)
            if numInput in y:
                return numInput
            else:
                print("Please enter a valid option")
        else:
            print("Please enter a valid option")

def create_players(x):    
    for i in range(x):
        players[f"player_{i + 1}"] = 0
    return players

def set_difficulty(x,y):
    while True:
        uInput = input(x)
        if uInput.isdigit():
            usrInput = int(uInput)
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
        else:
            print("Please enter a valid option")

def progress_bar(x):
    for _ in tqdm(range(x),desc="Loading positions",unit="s"):
        time.sleep(0.06)

def print_player(x):
    return "\n".join([f"{key}\t{value}" for key, value in x.items()])
    
def main_screen():
    print(f'''.::: Numerical Race :::.
Game difficulty: {levels} positions.
Players      Position
{print_player(players)}
''')

# def bonus_1_pair():
#     if (d1 + d2) % 2 == 0:


def in_game(x,y):
    gameOver = False
    while not gameOver:
        for player in x:
            os.system("clear")
            main_screen()
            if x[player] >= y:
                print(f"{player} is the winner")
                input("Press enter to exit...")
                break

            input(f"{player}, it's your turn!\nPress enter to roll")
            d1, d2 = roll_dices() 
            progres = d1 + d2
            x[player] += progres
            print(f"Dice 1: {d1}\nDice 2: {d2}\nGreat, advances {progres} positions")
            input("Press enter to next player")
            
            if x[player] >= y:
                os.system("clear")
                main_screen()
                print(f"{player} is the winner")
                gameOver = True
                break
            

#### main ####

players = {}

print(".::: Numerical Race :::.")
nplayers = create_players(valid_players("Multiplayer(2-4)\nEnter the number of players: ",[2,3,4]))

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



in_game(players, levels)

restart = input("Do you want to restart the game? y/n").lower()
if restart == "y":
    for player in players:
        players[player] = 0
    



        