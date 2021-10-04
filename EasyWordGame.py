#Ryan Taffe
#9/30/21
import random
num=random.randint(2,8)
print(num)
print("Welcome to hangman")
AvailableWords=["Elephant","Bathtub","Pencil","Texas"]
name= input("What is your name? ")
answer=input(name + ", would you like to play a game? ")
while ("y") in answer:
    word= AvailableWords[3]
    word=word.lower()
    turns=len(word)+2
    check = True
    guesses=" "
    while (turns>0 and check):
        for letter in word:
            if letter in guesses:
                print(letter, end=" ")
                if len(guesses)==len(word):
                    check = False
            else:
                print("_", end=" ")
        newGuess=input("\n Please enter a letter ")
        newGuess=newGuess.lower()
        if newGuess in word:
            guesses += newGuess
        else:
            turns -=1
            print("Sorry, guess again")
    print("You guessed right! The word was", word)
    answer=input(name + ", do you want to play again?")
print(name,", thank you for playing")