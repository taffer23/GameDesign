#Ryan Taffe
#Learning how to use while loops
print(" ")
print("Welcome! In this game you will have to guess an integer between 1 and 100")

name=input("What is your name? ")

print("Hi,", name)

answer=input("Do you want to play the game? ")
while('y' in answer):
    randy=1
    counter=0
    guess=input("Please enter an integer ")
    
    while(guess != randy):
        try:
            guess=int(guess)
            check=True
        except ValueError:
            check=False
        if guess == randy:
            print("You guessed correct! It took you")
            print(counter+1, end=" tries!")
        else:
            counter +=1
            if guess > randy:
                print("You guessed too high!")
            else:
                print("You guessed too low!")
            guess=input("Try again! ")
    print(" ")
    answer=input("Do you want to play again? ")
    while('n' in answer):
        break
print("Thank you for playing", name)
