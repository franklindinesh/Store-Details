from python_project_5 import *

print("Welcome to our Stores")
print("---------------------------")
print("* Store stock details *")
print("---------------------------")
x = {"product": [], "items": [], "quantity": []}
c = list(x.values())
product = c[0]
items = c[1]
quantity = c[2]

a = list(Fdstores)

for x in a:
    print(x)
print("---------------------------------------------")
b = input("Show the menu items : ")
# print(list(Fdstores[b]))

for y in Fdstores[b]:
    print(y)
print("----------------------------------------------")
n = input("availabe item : ")
print(Fdstores[b][n], " : Stock available")




















"""
print("welcome to our  FD stores  ")
a = list(Fdstores)
print(a)
print("------------------------")
print("Our Today products are:")

for x in Fdstores:
    print(x)
print("------------------------")
b = input("What do you want: ")
# print(FDStores[b].keys())
for y in Fdstores[b].keys():
    print(y)
c = input("Enter the item : ")

for z in Fdstores[b]["size"].items():
    print(z)

#for i in FDStores[b]["size"].values():
 #   print(i)

d = input("Select size : ")
print("-------------------------")

print(c, " : ", d)

print("-------------------------")
e = int(input("enter how many pack : ")) * int(input("enter pack size R.s: "))
print("Pay : ", e, "Rupees")

customer_amount = int(input("Enter the amount : ")) - e
print("Balance : ", customer_amount)
print("---------------------------")
print("---Thank you Visit Again---")



if e == 0:
    print("thanks")
elif e >= 100:
    print("pack is : ", e, "rupees")
    print("---Thank you visit again---")
elif e >= 500:
    print("pack is : ", e, "rupees")
    print("---Thank you visit again---")
elif e >= 1000:
    print("size pack is : ", e, "rupees")
    print("---Thank you visit again---")
else:
    print("not valid")
"""""
