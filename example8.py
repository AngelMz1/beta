'''
lista numeros teniendo en cuenta numero de inicio(li) y fin(ls) 
los numeros deben ser ingresados por el usuario
si el primer numero es mayor que el segundo se debe imprimir en orden descendente
'''
import os

os.system("clear")
print(".::: Inpresion de numeros :::.")

li = int(input("Ingrese el limite inferior: "))
ls = int(input("Ingrese el limite superior: "))
i = li
if li <= ls:
    while i <= ls:
        print(i)
        i += 1
else:
    while i >=ls:
        print(i)
        i -= 1