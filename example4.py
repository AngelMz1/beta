import os

def calc(x, y):
    #Process
    add = x + y

    return add
os.system("clear")
#Input
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

#Call function
ans = calc(num1, num2)

#Output
print(f"The addition is: {ans}")
print("The addition is: ", calc(num1, num2))
