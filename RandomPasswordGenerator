#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Storing random items from the list(letters):
RandomLetters = ""
for a in range(0,nr_letters):
  RandomLetters += random.choice(letters)

#Storing random items from the list(symbols):
RandomSymbols = ""
for b in range(0,nr_symbols):
  RandomSymbols += random.choice(symbols)

#Storing random items from the list(numbers):
RandomNumbers = ""
for c in range(0,nr_numbers):
  RandomNumbers += random.choice(numbers)
#Adding all the random elements extracted from these three lists in a variable:
Password = RandomLetters + RandomSymbols + RandomNumbers
#This will calculate the total number of password require:
TotalPassLen = nr_letters + nr_symbols + nr_numbers
#Initializing a string variable:
RandomPassword = ""
#Reshuffling the elements stored in a variable and storing into the declared string variable:
RandomPassword += ''.join(random.sample(Password,len(Password)))

print(f"Here is your {TotalPassLen} digits random password: {RandomPassword}")
