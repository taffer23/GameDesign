mport os, random

os.system ('cls')

for i in range(1):

    randy = random.randint(0,20)

    userInput = (input("Guess a number 1-20"))

    if userInput == randy:

        print("You guessed right!")

    else:

        print("You guessed wrong. Guess again!")

        userInput = (input("Guess a number 1-20"))

        print("You guessed wrong. Guess again!")

        userInput = (input("Guess a number 1-20"))

        print("You guessed wrong. Guess again!")

        userInput = (input("Guess a number 1-20"))

        print("You guessed wrong. Guess again!")

        userInput = (input("Guess a number 1-20"))

        print("You guessed wrong. Guess again!")

        userInput = (input("Guess a number 1-20"))

        print("You guessed wrong. Guess again!")

        userInput = (input("Guess a number 1-20"))

        print("You guessed wrong. Guess again!")

        userInput = (input("Guess a number 1-20"))

        print("You guessed wrong. Guess again!")

        userInput = (input("Guess a number 1-20"))

        print("You guessed wrong. Guess again!")

        userInput = (input("Guess a number 1-20"))

        print("You lose!")

    print(randy)