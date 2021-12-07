import pygame, os, time
import os, random
#K_UP, K_DOWN, K_RIGHT, K_LEFT uparrow downarrow rightarrow leftarrow
#Mouse position drawing rect moving object
import pygame as py
#Square is 200 high and 300 wide
#MUST USE FLIP FOR IMAGES
#First thing is to initiate
py.init
#Next create a window
walkLeft = [pygame.image.load('Images/Game/L1.png'), pygame.image.load('Images/Game/L2.png'), pygame.image.load('Images/Game/L3.png'), pygame.image.load('Images/Game/L4.png'), pygame.image.load('Images/Game/L5.png'), pygame.image.load('Images/Game/L6.png'), pygame.image.load('Images/Game/L7.png'), pygame.image.load('Images/Game/L8.png'), pygame.image.load('Images/Game/L9.png')]
walkRight = [pygame.image.load('Images/Game/R1.png'), pygame.image.load('Images/Game/R2.png'), pygame.image.load('Images/Game/R3.png'), pygame.image.load('Images/Game/R4.png'), pygame.image.load('Images/Game/R5.png'), pygame.image.load('Images/Game/R6.png'), pygame.image.load('Images/Game/R7.png'), pygame.image.load('Images/Game/R8.png'), pygame.image.load('Images/Game/R9.png')]
clock = pygame.time.Clock()
IsJump = False
JumpCount = 10
left = False
right = False
walkCount = 0
height = 600
width = 800
colors = {'red':(150,0,0),'green':(0,255,0),'purple':(150,0,150),'black':(0,0,0), 'white':(255,255,255), 'blue':(0,0,255)}
screen=py.display.set_mode((width, height))
myColor=colors.get('purple')
objectColor = colors.get("blue")
screen.fill(myColor)
py.display.set_caption("moving square")
py.display.update()
#Parameters to define our square
BoulderX = width-200
BoulderY = height-200
bg = pygame.image.load('Images/bgSmaller.jpg')
figx = 50
figy = 380
fig = pygame.image.load('Images/Game/standing.png')
screen.blit(bg, (0,0))
screen.blit(fig, (figx, figy))
Boulder = py.Rect(BoulderX,BoulderY, 200, 200)
py.draw.rect(screen, objectColor, Boulder)
py.display.update()

#Create boolean for jump, true or false depending on spacebar pressed

x = width/2
y = height/2
wbox=50
hbox = 50
square = py.Rect(x,y,wbox,hbox)
 #c54w6iny our object square
objColor = colors.get('red')
py.draw.rect(screen, objColor, square)
py.display.update()
# #Where, color, and object
# #Our object is red, it is in the screen, and it is a square
def redrawGameWindow():
    global walkCount
    screen.blit(bg, (0,0))
   
    if walkCount +1 >= 27:
        walkCount = 0

    if left:
        screen.blit(walkLeft[walkCount//3], (figx, figy))
        walkCount +=1
   
    elif right:
        screen.blit(walkRight[walkCount//3], (figx,figy))
        walkCount +=1
    else:
        screen.blit(fig, (figx, figy))
     #py.draw.circle(screen, circlecolor, (xc,yc), radius, width = 0)
    py.draw.rect(screen, objectColor, Boulder)
    py.display.flip()

# #Second rectangle
# x3 = random.randint(20,width)
# y3 = random.randint(20,height)
# rectangle2color=colors.get('blue')
# py.draw.rect(screen, rectangle2color, square)
# squaredos = py.Rect(x3,y3,wbox,hbox)
# #------------------
# #BUILDING A CIRCLE

# # circlecolor = colors.get('white')
# # xc = random.randint(20,width)
# # yc = random.randint(20,height)
# # radius = wbox/2
# # circle = py.draw.circle(screen, circlecolor, (xc,yc), radius)
# # py.display.update()

speed = 5



run = True
while run:
    clock.tick(27)
    for anyThing in py.event.get():
         if anyThing.type == py.QUIT:
             run = False
    keyPressed = py.key.get_pressed()
    #380y is floor
   
    if figx > width:
        figx = 0
    if figx < 0:
        figx = width
    if figy > 380:
        figy-=speed
    if figy < 0:
        figy = height
    if keyPressed[py.K_RIGHT]:
        figx += speed
        right = True
        left = False
   
    elif keyPressed[py.K_LEFT]:
        figx -= speed
        left = True
        right = False
    else:
        right = False
        left = False
    if keyPressed[py.K_UP]:
        figy -= speed
   
    if keyPressed[py.K_DOWN]:
        figy += speed
    if not (IsJump):
        if keyPressed[py.K_SPACE]:
            IsJump = True
            right = False
            left = False
            walkCount = 0   
    else:
        if JumpCount >= -10:
            figy -= (JumpCount * abs(JumpCount)) * 0.5
            JumpCount -= 1
        else: # This will execute if our jump is finished
            JumpCount = 10
            IsJump = False
    keyPressed = py.key.get_pressed()
    # if .colliderect(Boulder):
    #     square.y -=5
    #     figy -=5
    #     IsJump = False
    if figx > 600 and figy > 340:
        figy-=speed
    if figx >550 and figy > 340:
        figx-=speed
    if figy > 295 and figx >210 and figx < 150:
        figy -= speed
    if figx >90 and y >381:
        figx -= speed
    print(figx,figy)
    #screen.fill(myColor)
    redrawGameWindow()
           
py.quit()