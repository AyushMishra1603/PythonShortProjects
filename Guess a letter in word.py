import random

#Create a List
word_list = ["ardvark", "baboon", "camel"]

#Assign a random word from the list
chosen_word = random.choice(word_list)

#Take User's input and keep it in lower case
guess = input("Guess a letter:").lower()

#Run a loop and compare the word guessed by user with each letter of chosen word
for letter in chosen_word:
  if letter == guess:
    print("Correct guess!")
  else:
    print("Incorrect guess!")
print(chosen_word)
