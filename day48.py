print("🌟HIGH SCORE TABLE🌟")


scoreSheet = {}
while True:
  userName = input("Enter your name: ")
  if userName in scoreSheet:
    add = int(input("Add another score: "))
    scoreSheet[userName]["Score"].append(add)
  
  else:
    highScore = int(input("Enter your high score: "))
    scoreSheet[userName] = {"name":userName, "Score":[highScore]}
    
  goAgain = input("Do you want to add another score to the highscore table?").strip().lower()
  if goAgain == "y":
    continue
  elif goAgain == "n":
    break


file = open("highScore.txt", "a+")
file.write(f"{scoreSheet} \n")
file.close()






