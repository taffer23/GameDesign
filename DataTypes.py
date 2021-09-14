# Ryan Taffe
# Date: 9/14/21
# Data types and how to check for the right type of data

import os
os.system('cls')

#variable declare and initialize
num = 30
print(type(num))
num = 6.7
print(type(num))
userInput=input("type something")
#how to check for your data
try:
    userInput=float(userInput)
    print(type(userInput))
    check=True
except ValueError:
    check=False

#using conditional statement if/else
if (check):
    print(num + userInput)
else:
    print("Sorry I cannot add that number")

print(num/0)




#primitive data types
    #int is a number
    #float is a decimal
    #char is a character like a letter
    #string is a piece of code like ("hello")

