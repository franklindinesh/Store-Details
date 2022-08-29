from python_project_5 import *
#print("----------------------------------------------")
print("Welcome to our Stores")
print("---------------------------")
print("* Customer bill *")
print("---------------------------")

w = input("Enter the item name : ")
e = int(input("Enter how many pack : ")) * int(input("Enter pack size R.s: "))
print("Pay : ", e, "Rupees")

customer_amount = int(input("Customer pay amount : ")) - e
print("Balance : ", customer_amount, "Rupees")
print("---------------------------")
print("---Thank you Visit Again---")
