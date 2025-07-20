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

def print_player(x):
    return "\n".join([f"{key}\t{value}" for key, value in x.items()])
    
def main_screen():
    print(f'''.::: Numerical Race :::.
Game difficulty: {levels} positions.
Players      Position
{print_player(players)}
''')

def restart(x, y):
    while True:
        usrInput = input(x).lower()
        if usrInput in y:
            return usrInput
        else:
            print("Please enter a valid option.")

def bonus_dices():
    totalProgres = 0
    bonus = 0
    while True:
        d1, d2 = roll_dices()
        progres = d1 + d2
        totalProgres += progres
        input("Press enter to roll dices")
        print(f"Dice 1: {d1}, Dice 2: {d2}.")

        if d1 == d2:
            bonus += 1
            print("Great, you can throw again.")
        elif bonus == 3:
            print("Congratulations, you have won after getting three consecutive pairs.")
            return bonus
        else:
            break
    print(f"Great, you advanced {totalProgres} positions.")
    return totalProgres


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
            print(f"{player} is your turn...")
            progres = bonus_dices()
            bonus = 0
            if bonus == 3:
                x[player] = y
                break

            x[player] += progres
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

input("Everything ready. Press enter to start game")
os.system("clear")




restartGame = "y"
while restartGame == "y":
    in_game(players, levels)

    restartGame = restart("Do you want to restart the game? y/n: ",["y","n"])

    if restartGame == "n":
        break
    else:
        for player in players:
            players[player] = 0
    



        