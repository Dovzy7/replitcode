import os
import time 
import collections 


pokeInventory = []

def menu():
    print("--Pokemon Inventory--")
    print("1. Add")
    print("2. Remove ")
    print("3. View")
   


def add():
    item = input("What item would you like to add into your inventory?")
    pokeInventory.append(item)
    print(f"{item} has been added to your inventory!")

def remove():
    count = collections.Counter(pokeInventory)
    print(count)
    choice = input("What item would you like to remove from your inventory?")
    if choice in pokeInventory:
        pokeInventory.remove(choice)
        print(f"{choice} has been removed from your inventory!")
    else:
        print("Item not found")

    
def view():
    count = collections.Counter(pokeInventory)
    print(count)


while True:
    menu()
    try:
        choice = int(input("Enter your choice: (1, 2, 3)"))
        if choice == 1:
            add()

        elif choice == 2:
            remove()

        elif choice == 3:
            view()

        else:
            print("please enter a valid choice!")
            continue 

    except ValueError:
        print("Enter numerical values onlY!")
        continue 
    
    
    goAgain = input("Would u like to do something else within your inventory?(y/n)").strip().lower()
    if goAgain == "y":
        continue
    elif goAgain == "n":
        print("See you again soon!")

    else: 
        print("Invalid input! Please try again")
        continue 

    with open("Pokeinventory.txt","w") as file:
        file.write(str((pokeInventory)))

    break







        
    




    