from python_project_5 import *
print("Welcome to our Stores")
print("---------------------------")
print("* Upload details *")
print("---------------------------")


def showitem():
    a = list(Fdstores)
    for x in a:
        print(x)
    print("-----------------------------")
    w = input("Enter the items : ")
    b = Fdstores[w].keys()
    for b in Fdstores[w]:
        print(b)




def stockitem():
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

def addstockitems():
    a = list(Fdstores)
    for x in a:
        print(x)
    print("-----------------------------")

    w = input("Enter the items : ")
    b = Fdstores[w].keys()

    for b in Fdstores[w]:
        print(b)
    print("------------------------------")
    k = list(Fdstores[w])
    print(k)
    d = input("enter the item to add : ")
    print(d)
    z=k.append(d)
    print(z)
    print(k)
    for j in k:
        print(j)
    print("------------------------------")




while True:
    try:
        print("1.Show items\n2.Stockitems\n3.addstockitems\n4.Exit")
        print("-------------------")

        b = int(input("enter the choice : "))

    except ValueError:
        continue
    else:
        if b == 1:
            showitem()
            print("-------------------")
        elif b == 2:
            stockitem()
            print("---------------------")
        elif b == 3:
            addstockitems()
        else:
            print("---Well done---")
            quit()
            Fdstores.clear()
