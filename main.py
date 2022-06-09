from words import wordslist
from images import hman
import random

solution = str(random.sample(wordslist,1))

print(solution)

mistakes = 0

charList = []

for i in range(0,len(solution)):
  charList.append('_')




def gameLoop():
  print("---- Hangman -----")
  print(hman[mistakes])

  print("Your word: ", end="")
  for l in charList:
    print(l +" ", end="")

  guess = input("\nPlease choose a letter: ")


while "_" in charList and mistakes < 8:
  gameLoop()
