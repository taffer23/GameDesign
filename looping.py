#Ryan Taffe 9/8/21
#We are going to learn how to ask the user for an integer
#We are going to learn how to loop

star= int(input("Please enter number of stars ")) #allow to get values from the user

#print("* * * *")
#loop
#variable to count lines
line = star
for lncounter in range(line):
    for counter in range(star):
        print("*", end=" ")
    print( )
print("Thank you")
for lncounter in range(line):
    for counter in range(star):
        print("*", end=" ")
    print( )
    star = star-1
    #Also can use #star = star-1