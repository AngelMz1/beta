# Script description:
'''
1.Get 2 numbers (float or int)
2.Show main menu (1). add, (2). sub, (3). mul, (4). div
3.Select option
4.Create a function to get the result according with the option
5.Clear screen
'''
import os

def calc(x, y, z):
    if z > '5' or z < '1':
        ans = "Invalid option"
    elif z == '1':
        ans = x + y
    elif z == '2':
        ans = x - y
    elif z == '3':
        ans = x * y
    elif z == '4':
        if y == 0:
            ans = "Invalid operation"
        else:
            ans = x / y
    else:
        ans = x + y, x - y, x * y, x / y
    return ans
   
os.system("clear")
####### main ###########
num1 = float(input("Press first number: "))
num2 = float(input("Press second number: "))

print("::: Main menu :::")
print("[1]. Add [2]. Sub [3]. Mul [4]. Div [5]. All")

operation = input("Select an option: ")

res = calc(num1, num2, operation)
if operation == '5':
    print(f"The addition is: {res[0]} \n The subtraction is: {res[1]} \n The multiplication is: {res[2]} \n The division is: {res[3]}")
else:
    print(f"The result is: {res}")

