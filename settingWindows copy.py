#Fonts, blit, and creating functions

import pygame, os, time, random

pygame.init()

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
black=colors.get('black')
white=colors.get('white')
win=pygame.display.set_mode((width, height))
title_font=pygame.font.SysFont('comicsana', 80)
words_font=pygame.font.SysFont('comicsana', 40)
text=title_font.render("message", 1, black)
def display_title(message, x,y):
    pygame.time.delay(100)
    text=title_font.render(message, 1, colors.get('black'))
    win.blit(text, (x,y))
    pygame.display.update()
    pygame.time.delay(100)


run = True
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run=False

    win.fill(color)
    display_title("Settings", width/2-text.get_width()/2,40)
    pygame.time.delay(200)
    display_title("Dallas", width/2-text.get_width()/2,height/2)
    pygame.time.delay(200)
