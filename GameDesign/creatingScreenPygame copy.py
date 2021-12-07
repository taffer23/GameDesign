import pygame, os, time

#Initializes pygame
pygame.init()
os.system('cls')

#declare the object to display game
red = (255,0,0)
purple= (150,0,150)
#create a dictionary of colors)
#ask the user the size and the color for the window
color= input("What color do you prefer: red, blue, green, purple, white, black ")
check=True
while check:
    height= input("What is the height of your window? It must be between 100 and 1200. ")
    width= input("What is the width of your window? It must be between 100 and 1200. ")
    try:
        height= int(height)
        width= int (width)
        if height>100 and width>100 and height<1200 and width<1200:
            check=False
        else:
            print("Sorry, the value is not between 100 and 1200.")
    except ValueError:
        print("Sorry, enter a valid number.")


colors = {'red':(150,0,0),'green':(0,200,0), 'blue':(0,0,255), 'purple':(150,0,150), 'white':(255,255,255), 'black':(0,0,0) }
screen=pygame.display.set_mode((600,400))
screen=pygame.display.set_mode((width,height))
myColor= colors.get(color)
screen.fill(myColor)

pygame.display.update() #always use to update your screen

pygame.display.set_caption

run=True #Variable to control the main loop
while run:
    pygame.time.delay(1000) #milliseconds
    for anyThing in pygame.event.get():
        if anyThing.type ==pygame.QUIT:
            run = False

pygame.quit()
