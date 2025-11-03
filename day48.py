import os

with open("highscorev2.txt","a+") as file:
  while True:
    name = input("Enter your initials: ").strip()
    score = int(input("Enter your score: ")).strip()
    file.write(f"{name}\t")
    file.write(f"{score}\n")
    print("Added your name and score to the file! ")
    goAgain = input("Would you like to add another score? (y/n)").strip().lower()
    os.system("clear")
    if goAgain == "y":
      continue
    elif goAgain == "n":
      break
    else:
      print("Invalid input")
      continue 

  

  
  

