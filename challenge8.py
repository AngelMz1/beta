'''
1. Write a program that requests N integers in a vector.
2. If the new value to be entered is equal to the SUM of the last and 
second-to-last values entered, the system must request the number again
'''
import os
os.system("clear")
### functions ###
def valid_number():
    while True:
        num = input("Enter a number o [q] to exit: ").strip()
        if num.lower() == "q":
            break
        try:
            num = float(num)
            if len(numbers) >= 2 and num == numbers[-1] + numbers[-2]:
                print("The sum of the last two numbers is equal to the new number. Please enter a valid number.")
                raise ValueError
            else:
                numbers.append(num)
                os.system("clear")
                print("The numbers entered are: ",numbers)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
### main ###
numbers = []

valid_number()