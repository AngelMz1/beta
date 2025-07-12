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

lan = int(input("¿cuantas veces deseas lanzar los dados?: "))
i = 1
while i <= lan:

    d1 = randint(1,6)
    d2 = randint(1,6)

    print(f"lanzamiento {i}")
    print(f"dice 1 = {d1} \ndice 2 = {d2} \n")

    i += 1