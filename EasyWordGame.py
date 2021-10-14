#Ryan Taffe
#9/30/21
import os
import random
score=0

print("Welcome to Hangman")

HardestWords=["Elephant","Bathtub","Pencil","Texas"]
IntermediateWords=["Desk", "Wire", "Fast", "Shirt"]
EasyWords=["Box","Cat","Man","Dad"]
maxScore=0
name=input("What is your name? ")

def Menu():
    print("########################################")
    print("#        Choose a difficulty           #")
    print("#              1=Easy                  #")
    print("#             2=Medium                 #")
    print("#              3=Hard                  #")
    print("#            4=Scoreboard              #")
    print("#              5=Exit                  #")
    print("########################################")
    difficulty = input("Enter your choice ")
    try:
        difficulty=int(difficulty)
        check= True
    except ValueError:
        check= False
    if (check):
        return difficulty
    else:
        difficulty=Menu()


def selWord(difficulty):
    if difficulty==3:
        word=random.choice(HardestWords)
    elif difficulty==2:
        word=random.choice(IntermediateWords)
    elif difficulty==1:
        word=random.choice(EasyWords)
    return word

difficulty=Menu()
   
if difficulty==4:
    MyFile=open('score.txt','r')
    print(MyFile.read)()
    MyFile.close
    answer2=input("Are you ready to go back?")
    difficulty=Menu()
    #I couldn't figure out how to make this a function...
if difficulty==5:
    MyFile=open('score.txt', 'a')
    MyFile.write(name+ "\t Score: \t"+str(score))
    MyFile.write(score)
    MyFile.close
    os._exit
    print("Thank you for playing")
while difficulty <4:
    word = selWord(difficulty)
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
    if turns >0:
        print("You guessed right! The word was", word)
        score+=3*len(word)+5*turns
        print("Score: ", score)
        if score > maxScore:
            maxScore=score
    difficulty=Menu()
    if difficulty==4:
        MyFile=open('score.txt','r')
        print(MyFile.read)()
        MyFile.close
        answer2=input("Are you ready to go back?")
        difficulty=Menu()
    if difficulty==5:
        MyFile=open('score.txt', 'a')
        MyFile.write(name+ "\t Score: \t"+str(score))
        MyFile.write(score)
        MyFile.close    
        os._exit
        print("Thank you for playing")
