# Ryan Taffe
# Date: 09/17/2021
# Challege: Game 1


print("Welcome to The 1-20 Guessing Game! Guess the number 1-20 in less than 10 tries. Good Luck!")

randy = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

for i in range(10):
    userInput = (input("Guess a number 1-20"))
    try:
        userInput=int(userInput)
        check=True
    except ValueError:
        check=False

    if userInput == randy:
        print("You guessed right!")
        print("You won in")
        print(i+1)
        break
    else:
        print("You guessed wrong. Guess again!")
        userInput = (input("Guess a number 1-20"))
        print("You lose!")
        print("The number was")
        print(randy)
    