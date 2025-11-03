import os,time

highScore = 0
name = None 

with open("high.score","r") as file:
    contents = file.read().split("\n")

for rows in contents:
    data = rows.split()
    highScore += int(data[1])
    if int(data[1]) > highscore:
        





