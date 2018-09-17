
"""
File: guessTheNumber.py
Author: Rosanna Morey
guessing game non GUI - try to guess the random number "selected" by the computer
"""


import random
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint(smaller, larger)
count = 0
while True:
	count += 1
	userNumber = int(input("Enter your guess:"))
	if userNumber < myNumber:
		print("Too small!")
	elif userNumber > myNumber:
		print("Too large!")
	else:
		print("Congratulations! You've got it in", count, "tries!")
		break
		