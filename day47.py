import random, os
print("Welcome to the Pokemon battle simulator!")
print("You will be able to choose a Pokemon and then choose a stat to battle with.")
print("The Pokemon with the higher stat will win the battle.")
print("The Pokemon with the higher stat will win the battle.")
pokeOne = {"name": "DarkRai", "health": 100, "attack": 10, "defense": 5, "speed": 100}

pokeTwo = {"name": "Regigigas", "health": 150, "attack": 4, "defense": 7, "speed": 30}

while True:
  userChoice = int(input("Do you want to battle with 1. DarkRai or 2. Regigigas? (Enter 1 or 2:"))
  if userChoice == 1:
    userPoke = pokeOne
    cpuPoke = pokeTwo
  elif userChoice == 2:
    userPoke = pokeTwo
    cpuPoke = pokeOne
  else: 
    print("Invalid choice. Please enter 1 or 2.")
    continue
  print()
  print(f"You chose {userPoke['name']}!")
  chooseStat = int(input("Choose a stat to battle with: 1. Attack, 2. Defense, 3. Speed (Enter 1, 2, or 3): "))
  if chooseStat == 1:
    print(f"{userPoke['name']} has {userPoke['attack']} attack! {cpuPoke['name']} has {cpuPoke['attack']} attack!")
    if userPoke["attack"] > cpuPoke["attack"]:
      print(f"{userPoke['name']} has an attack stat of {userPoke['attack']} and {cpuPoke['name']} has an attack stat of {cpuPoke['attack']}.")
      print()
      print(f"{userPoke['name']} wins!") 
    else:
      print(f"{userPoke['name']} has {userPoke['attack']} attack! {cpuPoke['name']} has {cpuPoke['attack']} attack!")
      print()
      print(f"{cpuPoke['name']} wins!")
    goAgain = input("Do you want to go again? (y/n): ").strip().lower()
    if goAgain != "y":
      continue
    else:
      print("Thanks for playing! ")
      break
  elif chooseStat == 2:
    print(f"{userPoke['name']} has {userPoke['defense']} defense! {cpuPoke['name']} has {cpuPoke['defense']} defense!")
    if userPoke["defense"] > cpuPoke["defense"]:
      print(f"{userPoke['name']} has {userPoke['defense']} defense! {cpuPoke['name']} has {cpuPoke['defense']} defense!")
      print()
      print(f"{userPoke['name']} wins!")
    else:
      print(f"{userPoke['name']} has {userPoke['defense']} defense! {cpuPoke['name']} has {cpuPoke['defense']} defense!")
      print()
      print(f"{cpuPoke['name']} wins!")
    goAgain = input("Do you want to go again? (y/n): ").strip().lower()
    if goAgain != "y":
      continue
    else:
      print("Thanks for playing! ")
      break
  elif chooseStat == 3:
    print(f"{userPoke['name']} has {userPoke['speed']} speed! {cpuPoke['name']} has {cpuPoke['speed']} speed!")
    if userPoke["speed"] > cpuPoke["speed"]:
      print(f"{userPoke['name']} has {userPoke['speed']} speed! {cpuPoke['name']} has {cpuPoke['speed']} speed!")
      print()
      print(f"{userPoke['name']} wins!")
    else:
      print(f"{userPoke['name']} has {userPoke['speed']} speed! {cpuPoke['name']} has {cpuPoke['speed']} speed!")
      print()
      print(f"{cpuPoke['name']} wins!")
    goAgain = input("Do you want to go again? (y/n): ").strip().lower()
    if goAgain != "y":
      continue
    else:
      print("Thanks for playing! ")
      break
  
  elif chooseStat == 4:
    print(f"{userPoke['name']} has {userPoke['health']} health! {cpuPoke['name']} has {cpuPoke['health']} health!")
    if userPoke["health"] > cpuPoke["health"]:
      print(f"{userPoke['name']} has {userPoke['health']} health! {cpuPoke['name']} has {cpuPoke['health']} health!")
      print()
      print(f"{userPoke['name']} wins!")
    else:
      print(f"{userPoke['name']} has {userPoke['health']} health! {cpuPoke['name']} has {cpuPoke['health']} health!")
      print()
      print(f"{cpuPoke['name']} wins!")
  goAgain = input("Do you want to go again? (y/n): ").strip().lower()
  if goAgain != "y":
    continue
  else:
    print("Thanks for playing! ")
    break
    
    
    
  
      
  
  
  