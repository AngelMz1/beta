#### Repot in python ###

#### Imports ####
import os
from random import randint

#### Functions ####
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

def numb_valid(x):
    while True:
        entry =input(x).strip()
        try:
            number = float(entry)
            return number
        except:
            print("Invalid data, please try again")

def age_valid(x):
    while True:
        entry =input(x).strip()
        try:
            age = int(entry)
            if age >= 18 and age <= 100:
                return age
            else:
                print("Age out of range, please try again")
        except:
            print("Invalid data, please try again")

def save_client(a,b,c,d,e,f,g,h,i,j):
    customer = {
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
    allCustomers[f"customer{j}"] = customer
    print(f"customer{j} ")
    print(allCustomers)

#### main screen ####
os.system("clear")
print(".::: Python report generator script  :::.")
print("Athen enter the customer data: ")
input("Press enter to start...")

#### data entry ####
allCustomers = {}
employee = 0
next = True
while next:
    os.system("clear")
    fullName = data_valid("Enter the full name: ")
    idNumber = data_valid("Enter the ID number: ")
    age = age_valid("Enter the age: ")
    movilPhone = data_valid("Enter the mobile phone: ")
    address = data_valid("Enter the address: ")
    customerStatus = True
    income = get_income()
    expenses = float(numb_valid("Enter the expenses: "))
    balance = income - expenses
    employee += 1
    save_client(fullName, idNumber, age, movilPhone, address, customerStatus, income, expenses, balance, employee)
    ans = input("Do you want to add another customer? \n"
    "Press [y] to add or any other key to continue...").lower()
    if ans != "y":
        next = False


#### report generator ####
os.system("clear") 

print("::: Report generator :::")
print("::: Customers list :::")

for value in allCustomers.values():
    print(f"Customer: {value['Id']} \n Name: {value['Name']} \n Id Number: {value['Id Number']} \n Age: {value['Age']} \n Movil Phone: {value['Movil Phone']} \n Address: {value['Address']} \n Client Status: {value['Client Status']} \n Income: {value['Income']} \n Expenses: {value['Expenses']} \n Balance: {value['Balance']} \n")

input("End of report, press enter to exit")

