####Repot in python###

import os
from random import randint

def get_income():
    income = randint(1000000,8000000)
    return income

def data_valid(x):
    while True:
        entry =input(x).strip()
        if entry :
            return entry
        else:
            print("Invalid data, please try again")
def save_client(a,b,c,d,e,f,g,h,i,j):
    client = {
        "Name": a,
        "Id Number": b,
        "Age": c,
        "Movil Phone": d,
        "Address": e,
        "Client Status": f,
        "Income": g,
        "Expenses": h,
        "Balance": i,
        "Id": j
    }
    allClient = client
    print(allClient)
### input data ###
os.system("clear")
print(".::: Python report generator script  :::.")
print("Athen enter the client data: ")
input("Press enter to start...")
allClient = {}
employee = 0
next = True
while next:
    os.system("clear")
    fullName = data_valid("Enter the full name: ")
    idNumber = data_valid("Enter the ID number: ")
    age = int(data_valid("Enter the age: "))
    movilPhone = data_valid("Enter the mobile phone: ")
    address = data_valid("Enter the address: ")
    clientStatus = True
    income = get_income()
    expenses = float(data_valid("Enter the expenses: "))
    balance = income - expenses
    employee += 1
    save_client(fullName, idNumber, age, movilPhone, address, clientStatus, income, expenses, balance, employee)
    ans = input("Do you want to add another client? \n"
    "Press [y] to add or any other key to exit...").lower()
    if ans != "y":
        next = False