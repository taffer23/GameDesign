# Ryan Taffe
# 10/6/2021
# We are going to learn how to 
#   write ('w)
#   read('r')
#   append('a')
#   close()
import os, time

#To create a file you must declare a variable name so we can open the file
#This is the way to open and create a file
myFile=open('score.txt', 'w')
myFile.write("Hello there, \nMy name is Ryan \t 1224")
myFile.close()#Always close your file as soon as you don't need it anymore
#This is the way to open and read a file
myFile=open('score.txt', 'r')
print(myFile.read())
myFile.close()
#Write things on the file, 'w' will delete what is on the file and write over it
anotherFile=open('score.txt', 'w')
anotherFile.write('Sorry, I changed my mind')
anotherFile.close()
#reprint
myFile=open('score.txt', 'r')
print(myFile.read())
myFile.close()
#append
anotherFile=open('score.txt', 'a')
anotherFile.write("\nLet's try again\nThe score is:\t23")
anotherFile.close()
myFile=open('score.txt', 'r')
print(myFile.readline())
print(myFile.readline())
myFile.close()