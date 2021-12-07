#K_UP                  up arrow
#K_DOWN                down arrow
#K_RIGHT               right arrow
#K_LEFT                left arrow

import os
import pygame as py
import random
from pygame import color

from pygame.draw import circle



py.init()

height = 800
width = 800
colors = {'red':(150,0,0),'green':(0,200,0), 'blue':(0,0,255), 'purple':(150,0,150), 'white':(255,255,255), 'black':(0,0,0) }
screen=py.display.set_mode((width,height))
myColor= colors.get('blue')
screen.fill(myColor)
py.display.set_caption("Moving square")
py.display.flip()
#parameters to define our square

x=width/2
y=height/2
wbox=50
hbox=50
#creaitng our object square
square=py.Rect(x,y,wbox,hbox)
#draw rectangle
# py.draw.rect()
objColor=colors.get('green')
py.draw.rect(screen, objColor, square)
py.display.update()
#create speed to move the object on the screen
speed = 5
rad=wbox/2
xc=random.randint(10,width)
yc=random.randint(10,height)
circleColor=colors.get('white')



run=True #Variable to control the main loop
while run:
    py.time.delay(20) #milliseconds
    for anyThing in py.event.get():
        if anyThing.type ==py.QUIT:
            run = False

    keyPressed= py.key.get_pressed()
    if keyPressed[py.K_RIGHT]:
        square.x += speed
    if keyPressed[py.K_LEFT]:
        square.x -= speed
    if keyPressed[py.K_UP]:
        square.y -= speed
    if keyPressed[py.K_DOWN]:
        square.y += speed
    if square.x>width:
        square.x=0
    if square.y<0:
        square.y=height
    if square.x<0:
        square.x=width
    if square.y>height:
        square.y=0

    if keyPressed[py.K_d]:
        xc += speed
    if keyPressed[py.K_a]:
        xc -= speed
    if keyPressed[py.K_w]:
        yc -= speed
    if keyPressed[py.K_s]:
        yc += speed
    if xc>width:
        xc=width-5
    if yc<0:
        yc=0+5
    if xc<0:
        xc=0+5
    if yc>height:
        yc=height-5
    collide= py.Rect.collidepoint(square,(xc,yc))
    if collide:
        square.x= random.randint(25,550)
        square.y= random.randint(25,550)
        rad= rad+25
        if rad >= 175:
            print("You win!")
            run=False

    
    ##if pygame.Rect.collidepoint(rect,(xc,yc)):
       #     xc=wbox/2
      #      yc=50
     #   print("I got you!")
    #if yc==square.y:
    ##    print("I got you!")
    #square.x=random.randint(10,width)
    #

    screen.fill(myColor)
    py.draw.circle(screen, circleColor, (xc,yc), rad, width=0)
    py.draw.rect(screen, objColor, square)
    py.display.update()
py.quit()
