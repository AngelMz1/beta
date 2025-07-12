'''
script description
crea un script que lance los dados n veces y visualice los resultados.
cantidad o numero de veces deve ser ingresada por el usuario
deben lanzarce dos  dado 
implementa funciones
'''
import os
from random import randint

os.system("clear")

def get_dices():
    d1 = randint(1,6)
    d2 = randint(1,6)
    return d1, d2

def valid_input(x, y):
    while True:
        uans = input(x).lower()
        if uans in y:
            return uans


next = True
i = 0

while next:
    d1, d2 = get_dices()
    i += 1
    print(f"lanzamiento {i}")
    print(f"dice 1 = {d1} \ndice 2 = {d2} \n")

    ans = valid_input("Desea lanzar nuevamente? [s/S/n/N]", ["s", "n"])
    
    if ans == "n":
        break
    
    

print(f"Usted lanzó los dados {i} veces")
    