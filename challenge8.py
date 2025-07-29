'''
1. Write a program that requests N integers in a vector.
2. If the new value to be entered is equal to the SUM of the last and 
second-to-last values entered, the system must request the number again
'''
### functions ###

### main ###
numbers = []

while True:
    num = int(input("Enter an integer: "))
    if len(numbers) >= 2 and num == numbers[-1] + numbers[-2]:
        print("The number entered is equal to the sum of the last two numbers.")
        break
    numbers.append(num)