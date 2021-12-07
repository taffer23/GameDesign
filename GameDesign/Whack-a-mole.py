import pygame, os, random, time

#Add screen size and backgroun color

#create a window for setting in your game
os.system('cls')
pygame.init()
DISPLAY_MAIN_MENU=0
DISPLAY_INSTRUCTIONS=1
DISPLAY_LEVEL_1=2
DISPLAY_LEVEL_2=3
DISPLAY_SETTINGS=4
DISPLAY_LEADERBOARD=5
#EXIT?
DISPLAY_SCREEN_SIZE=6
DISPLAY_SETTINGS_BACKGROUND_COLOR=7
DISPLAY_OBJECT_COLORS=8
DISPLAY_SOUNDS_ON_OFF=9
DISPLAY_WINDOW_SIZE=10
#BACK?

mole=pygame.image.load('Images/mole.png')


currentDisplay = DISPLAY_MAIN_MENU



## LISTS FOR MENU MESSAGES
MainMenuMessages=["Instructions", "Level 1", "Level 2", "Settings", "Leaderboard","Exit"]
Settings=["Screen Size", "Background Color"]
WindowSize=["800 x 800", "850 x 850", "900 x 900"]
BackgroundColors=["Green", "Blue", "White"]
ObjectColors=["Red", "Green", "Blue", "Purple", "White", "Black", "Orange"]
SoundsOnOff=["Sounds On", "Sounds Off"]


#global variables
colors = {'red':(150,0,0),'green':(0,200,0), 'blue':(0,0,255), 'purple':(150,0,150), 'white':(255,255,255), 'black':(0,0,0), 'orange':(255,155,0)}
WHITE=colors.get('white')
BLACK=colors.get('black')
GREEN=colors.get('green')
ORANGE=colors.get('orange')
BLUE=colors.get('blue')
COLOR=WHITE

counter=1

WIDTH=800
HEIGHT=800
wbox=30
hbox=30
x=70
y=150
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Welcome to Whack a Mole!")
square=pygame.Rect(x,y, wbox, hbox)

#Declare FONTS
TITLE_FONT=pygame.font.SysFont('comicsans', 80)
MENU_FONT=pygame.font.SysFont('comicsans', 40)
text=TITLE_FONT.render('message',1,BLACK)

def display_Title(message,ym):
    pygame.time.delay(100)
    text=TITLE_FONT.render(message,1,BLACK)
    xm=WIDTH/2-text.get_width()/2
    win.blit(text, (xm,ym))
    pygame.display.update()
    pygame.time.delay(100)

def Menu_function(Messages,y):
    
    pygame.time.delay(100)
    
    square.y=y
    ym=y
    xm=x+wbox+10
    for i in range(0,len(Messages)):
        word=Messages[i]
        pygame.draw.rect(win,ORANGE, square)
        text=MENU_FONT.render(word,1,BLACK)
        win.blit(text, (xm,ym))
        pygame.display.update()
        pygame.time.delay(100)
        ym +=100
        square.y=ym

def create_NewWindow(windowtitle):
    pygame.display.set_caption(windowtitle)
    win.fill(COLOR)
    pygame.display.update
win.fill(COLOR)
display_Title("Welcome to Whack a Mole!",40)
Menu_function(MainMenuMessages, 150)

pygame.time.delay(300)
currentDisplay == DISPLAY_MAIN_MENU
run=True
while run:
    for eve in pygame.event.get():
        if eve.type == pygame.QUIT:
            run=False
        if eve.type ==pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                mouse_pos =pygame.mouse.get_pos()
                print(mouse_pos)
                xp=mouse_pos[0]
                yp=mouse_pos[1]
                if currentDisplay == DISPLAY_MAIN_MENU:
                    if xp>x and xp<x+wbox and yp>y and yp<245:
                        xp = 0
                        yp = 0
                        create_NewWindow("Instructions")
                        win.fill(COLOR)
                        display_Title("Instructions",40)
                        display_Title("BACK",HEIGHT-100)
                        currentDisplay=DISPLAY_INSTRUCTIONS
                    
                    if xp>=70 and xp<x+wbox and yp>250 and yp<=275:
                        xp = 0
                        yp = 0
                        create_NewWindow("Level 1")
                        win.fill(COLOR)
                        display_Title("Level 1",40)
                        display_Title("BACK",HEIGHT-100)                 
                        currentDisplay=DISPLAY_LEVEL_1
                    if xp>=70 and xp<x+wbox and yp>350 and yp<375:
                        xp = 0
                        yp = 0
                        create_NewWindow("Level 2")
                        win.fill(COLOR)
                        display_Title("Level 2",40)
                        display_Title("BACK",HEIGHT-100)
                        currentDisplay=DISPLAY_LEVEL_2
                    if xp>=x and xp<x+wbox and yp>450  and yp<475:
                        xp = 0
                        yp = 0
                        create_NewWindow("Settings")
                        display_Title("Settings",40)
                        display_Title("BACK",HEIGHT-100)
                        Menu_function(Settings,150)
                        currentDisplay=DISPLAY_SETTINGS
                    if xp>=x and xp<x+wbox and yp>550  and yp<575:
                        xp = 0
                        yp = 0
                        create_NewWindow("Leaderboard")
                        win.fill(COLOR)
                        display_Title("Leaderboard",40)
                        display_Title("BACK",HEIGHT-100)
                        currentDisplay=DISPLAY_LEADERBOARD
                    if xp>=x and xp<x+wbox and yp>650  and yp<675:
                        xp = 0
                        yp = 0
                        #update your score file
                        run=False
                if currentDisplay==DISPLAY_INSTRUCTIONS:
                    myFile=open('Whack-a-mole-instructions.txt','r')
                    yi=150
                    for line in myFile.readlines():
                        text=MENU_FONT.render(line, 1, BLACK)
                        win.blit(text, (40,yi))
                        pygame.display.update()
                        pygame.time.delay(100)
                        yi+=50
                    myFile.close()
                        
                    if xp>=WIDTH/2-40 and xp<WIDTH/2+50 and yp>HEIGHT-100 and yp<HEIGHT-50:
                        xp = 0
                        yp = 0
                        DISPLAY_MAIN_MENU=True
                        DISPLAY_INSTRUCTIONS=False
                        win.fill(COLOR)
                        display_Title("Welcome to Whack a Mole!",40)
                        Menu_function(MainMenuMessages, 150)
                        pygame.display.set_caption("Welcome to Whack a Mole!")
                        currentDisplay=DISPLAY_MAIN_MENU











                #Level 1
                if currentDisplay==DISPLAY_LEVEL_1:

                    bg1 = pygame.image.load('Background.png')
                    win.blit(bg1, (0,0))
                    molex= (400)
                    moley= (200)
                   # molex= random.randint(0,800)
                   # moley= random.randint(0,400)
                    win.blit(mole, (molex, moley))
                    pygame.display.set_caption("Level 1")
                    pygame.display.flip()
                            
                    if xp>=molex and xp<50+molex and yp>moley and yp<=moley+25:
                        molex= random.randint(0,800)
                        moley= random.randint(0,400)
                        win.blit(mole, (molex, moley))
                        

                    if xp>=WIDTH/2-40 and xp<WIDTH/2+50 and yp>HEIGHT-100 and yp<HEIGHT-50:
                        xp = 0
                        yp = 0
                        win.fill(COLOR)
                        display_Title("Welcome to Whack a Mole!",40)
                        Menu_function(MainMenuMessages, 150)
                        pygame.display.set_caption("Welcome to Whack a Mole!")
                        currentDisplay=DISPLAY_MAIN_MENU
































                #Level 2            
                if currentDisplay==DISPLAY_LEVEL_2:
                    bg1 = pygame.image.load('Background.png')

                        
                    win.blit(bg1, (0,0))
                    pygame.display.set_caption("Level 2")
                    pygame.display.flip()
                            
                    if xp>=WIDTH/2-40 and xp<WIDTH/2+50 and yp>HEIGHT-100 and yp<HEIGHT-50:
                        xp = 0
                        yp = 0
                        win.fill(COLOR)
                        display_Title("Welcome to Whack a Mole!",40)
                        Menu_function(MainMenuMessages, 150)
                        pygame.display.set_caption("Welcome to Whack a Mole!")
                        currentDisplay=DISPLAY_MAIN_MENU
                            









































                if currentDisplay==DISPLAY_SETTINGS:
                    if xp>=WIDTH/2-40 and xp<WIDTH/2+50 and yp>HEIGHT-100 and yp<HEIGHT-50:
                        xp = 0
                        yp = 0
                        win.fill(COLOR)
                        display_Title("Welcome to Whack a Mole!",40)
                        Menu_function(MainMenuMessages, 150)
                        pygame.display.set_caption("Welcome to Whack a Mole!")
                        currentDisplay=DISPLAY_MAIN_MENU

                    if xp>x and xp<x+wbox and yp>y and yp<245:
                        xp = 0
                        yp = 0
                        create_NewWindow("Screen Size")
                        win.fill(COLOR)
                        display_Title("Screen Size",40)
                        display_Title("BACK",HEIGHT-100)
                        Menu_function(WindowSize, 150)
                        currentDisplay=DISPLAY_SCREEN_SIZE

                    if xp>=70 and xp<x+wbox and yp>250 and yp<=275:
                        xp = 0
                        yp = 0
                        create_NewWindow("Background Color")
                        win.fill(COLOR)
                        display_Title("Background Color",40)
                        display_Title("BACK",HEIGHT-100)  
                        Menu_function(BackgroundColors, 150)               
                        currentDisplay=DISPLAY_SETTINGS_BACKGROUND_COLOR
                    

                if currentDisplay==DISPLAY_SCREEN_SIZE:
                    
                    
                    #if xp>=WIDTH/2-40 and xp<WIDTH/2+50 and yp>HEIGHT-100 and yp<HEIGHT-50:
                     #   xp = 0
                     #   yp = 0
                     #   win.fill(COLOR)
                     #   display_Title("Welcome to Whack a Mole!",40)
                     #  Menu_function(MainMenuMessages, 150)
                     #   pygame.display.set_caption("Welcome to Whack a Mole!")
                     #    currentDisplay=DISPLAY_MAIN_MENU
                    
                    if xp>x and xp<x+wbox and yp>y and yp<245:
                        xp = 0
                        yp = 0
                        WIDTH = 800
                        HEIGHT = 800
                        win=pygame.display.set_mode((WIDTH,HEIGHT))
                        pygame.display.flip()
                        xp = 0
                        yp = 0
                        create_NewWindow("Screen Size")
                        win.fill(COLOR)
                        display_Title("Screen Size",40)
                        display_Title("BACK",HEIGHT-100)
                        Menu_function(WindowSize, 150)
                        currentDisplay=DISPLAY_SCREEN_SIZE

                    if xp>=70 and xp<x+wbox and yp>250 and yp<=275:
                        xp = 0
                        yp = 0
                        WIDTH = 850
                        HEIGHT = 850
                        win=pygame.display.set_mode((WIDTH,HEIGHT))
                        pygame.display.flip()
                        xp = 0
                        yp = 0
                        create_NewWindow("Screen Size")
                        win.fill(COLOR)
                        display_Title("Screen Size",40)
                        display_Title("BACK",HEIGHT-100)
                        Menu_function(WindowSize, 150)
                        currentDisplay=DISPLAY_SCREEN_SIZE

                    if xp>=70 and xp<x+wbox and yp>350 and yp<375:
                        xp = 0
                        yp = 0
                        WIDTH = 900
                        HEIGHT = 900
                        win=pygame.display.set_mode((WIDTH,HEIGHT))
                        pygame.display.flip()
                        xp = 0
                        yp = 0
                        create_NewWindow("Screen Size")
                        win.fill(COLOR)
                        display_Title("Screen Size",40)
                        display_Title("BACK",HEIGHT-100)
                        Menu_function(WindowSize, 150)
                        currentDisplay=DISPLAY_SCREEN_SIZE

                    if xp>=WIDTH/2-40 and xp<WIDTH/2+50 and yp>HEIGHT-100 and yp<HEIGHT-50:
                        xp = 0
                        yp = 0
                        win.fill(COLOR)
                        display_Title("Welcome to Whack a Mole!",40)
                        Menu_function(MainMenuMessages, 150)
                        pygame.display.set_caption("Welcome to Whack a Mole!")
                        currentDisplay=DISPLAY_MAIN_MENU

                if currentDisplay==DISPLAY_SETTINGS_BACKGROUND_COLOR:


                    if xp>x and xp<x+wbox and yp>y and yp<245:
                        xp = 0
                        yp = 0
                        COLOR=GREEN

                    if xp>=70 and xp<x+wbox and yp>250 and yp<=275:
                        xp = 0
                        yp = 0
                        COLOR=BLUE

                    if xp>=70 and xp<x+wbox and yp>350 and yp<375:
                        xp = 0
                        yp = 0
                        COLOR=WHITE

                    win.fill(COLOR)
                    display_Title("Background Color",40)
                    display_Title("BACK",HEIGHT-100)  
                    Menu_function(BackgroundColors, 150)

                    if xp>=WIDTH/2-40 and xp<WIDTH/2+50 and yp>HEIGHT-100 and yp<HEIGHT-50:
                        xp = 0
                        yp = 0
                        win.fill(COLOR)
                        display_Title("Welcome to Whack a Mole!",40)
                        Menu_function(MainMenuMessages, 150)
                        pygame.display.set_caption("Welcome to Whack a Mole!")
                        currentDisplay=DISPLAY_MAIN_MENU

                if currentDisplay==DISPLAY_LEADERBOARD:
                    myFile=open('Whack-a-mole-leaderboard.txt','r')
                    yi=150
                    for line in myFile.readlines():
                        text=MENU_FONT.render(line, 1, BLACK)
                        win.blit(text, (40,yi))
                        pygame.display.update()
                        pygame.time.delay(100)
                        yi+=50
                    myFile.close()

                    if xp>=WIDTH/2-40 and xp<WIDTH/2+50 and yp>HEIGHT-100 and yp<HEIGHT-50:
                        xp = 0
                        yp = 0
                        win.fill(COLOR)
                        display_Title("Welcome to Whack a Mole!",40)
                        Menu_function(MainMenuMessages, 150)
                        pygame.display.set_caption("Welcome to Whack a Mole!")
                        currentDisplay=DISPLAY_MAIN_MENU              


pygame.quit()