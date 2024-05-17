import random
import sys

print("Welcome to Hangman")

numOfAttempt = input("Enter the Number of Attempt : ")

try:
  numOfAttempt = int(numOfAttempt)
except :
  print("Enter Numeric value only")
  sys.exit(0)

words = ["elephant", "apple", "computer", "college"]
# print(words)

rnWord = random.choice(words)
lenOfString = len(rnWord)
indexOfrnWord = words.index(rnWord)

hint = ["Has a trunk","fruit","Electronic device","Place of knowlege"]
print("Hint : ",hint[indexOfrnWord])

newList = list('_' * lenOfString)

hangMan = 0

def hangman(n, m):
  print('__________')
  if (n > 0 or m <= 3):
    print('|        |\n' * (n - 1) + '|        |')
  if (m <= 2):
    print('|        O')
  if (m <= 1):
    print('|       /|\\')
  if (m <= 0):
    print('|       / \\')

def lenOfNewList(newList):
  countOfNewList = 0
  for n in newList:
    if (n.isalpha()):
      countOfNewList += 1
  return countOfNewList

while lenOfString != lenOfNewList(newList) and numOfAttempt > 0:
  newWord = input("Enter a Letter ( Enter 'QUIT' to exit ) : ")
  if (newWord == "QUIT"):
    print("Game Exit")
    sys.exit(0)
  print("Word : ")
  if newWord in rnWord:
    countOfNewWordInrnWord = rnWord.count(newWord)
    for i, v in enumerate(rnWord):
      if countOfNewWordInrnWord >= 0 and newWord == v:
        newList.pop(i)
        newList.insert(i, v)
        countOfNewWordInrnWord = countOfNewWordInrnWord - 1
    print("".join(newList))
    print("Good Guess")
    hangman(hangMan, numOfAttempt)
  else:
    print("".join(newList))
    print(f"sorry the letter {newWord} is not in word")
    numOfAttempt -= 1
    hangMan += 1
    hangman(hangMan, numOfAttempt)

if (numOfAttempt > 0):
  print("Congratulations! you have guessed the word !!!🎉")
else:
  print("Reached the limit of number of attemps")
