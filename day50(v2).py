import os,time,random


ideaStorage = ["Monkey Tennis", "Bootleg Pokemon", "OnlyFans Clone"]

with open("myIdeas.txt","a+") as file:
    for idea in ideaStorage:
        file.write(f"{idea}\n")

while True:
    print("Idea Storage")
    print("1. Add An Idea")
    print("2. See a random idea")

    choice = int(input("Pick your choice"))
    if choice == 1:
        add = input("What is that grand idea you would like to add to list of ideas?")
        if add not in ideaStorage:
            ideaStorage.append(add)
            print("Your Idea has been stored.")
            with open("myIdeas.txt","a+") as file:
                file.write(f"{add}\n")
           
        
        else:
            print("This idea is already in the void of ideas")

    elif choice == 2:
        print(random.choice(ideaStorage))
        time.sleep(5)
        os.system("clear")

    else:
        print("Invalid choice. Please try again!")
        continue

    
    
    goAgain = input("Do you want to add another idea? (y/n)").strip().lower()

    if goAgain == "y":
        continue

    elif goAgain == "n":
        break




print("Thank you for using the infinity idea void!")
time.sleep(5)
os.system("clear")

    