# import random module
from random import randint, shuffle

# generate a list of alphabet letters in lower and uppercase
letters = [chr(i) for i in range(ord('A'), ord('Z')+1)] + [chr(i) for i in range(ord('a'), ord('z')+1)]

# generate a list of integers from 0 to 9
numbers = [i for i in range(0,10)]

# generate a list of special characters
symbols = [chr(i) for i in range(33, 41)]

# introduction
print("Welcome to the Password Generator Tool!")

# get password properties
numberOfLetters = int(input("How many letters would you like in your password?\n"))
numberOfNumbers = int(input("How many numbers would you like in your password?\n"))
numberOfSymbols = int(input("How many symbols would you like in your password?\n"))

# placeholder objects
passwordLetters = str()
passwordNumbers = int()
passwordSymbols = str()

# generate parts of the password
for i in range(0, numberOfLetters):
  passwordLetters += letters[randint(0, len(letters)-1)]
for i in range(0, numberOfNumbers):
  passwordNumbers += numbers[randint(0, len(numbers)-1)]
for i in range(0, numberOfSymbols):
  passwordSymbols += symbols[randint(0, len(symbols)-1)]

# concatenate all three string variables
combinedPassword = passwordLetters + str(passwordNumbers) + passwordSymbols

# placeholder password
passwordCharacters = list(combinedPassword)

# shuffle elements of the passwordCharacters list
shuffle(passwordCharacters)

# create the password
password = ''.join(passwordCharacters)

# print the password
print(f"\nYour password is: {password}")