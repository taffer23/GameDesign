import pygame, os, random, time


#create a window for setting in your game
os.system('cls')
pygame.init()
DISPLAY_MAIN_MENU=0
DISPLAY_INSTRUCTIONS=1
DISPLAY_LEVEL_1=2
DISPLAY_LEVEL_2=3
DISPLAY_SETTINGS=4
DISPLAY_SCOREBOARD=5
#EXIT?
DISPLAY_SCREEN_SIZE=6
DISPLAY_SETTINGS_BACKGROUND_COLOR=7
DISPLAY_OBJECT_COLORS=8
DISPLAY_SOUNDS_ON_OFF=9
DISPLAY_WINDOW_SIZE=10
#BACK?
currentDisplay = DISPLAY_MAIN_MENU



## LISTS FOR MENU MESSAGES
MainMenuMessages=["Instructions", "Level 1", "Level 2", "Settings", "Scoreboard","Exit"]
Settings=["Screen Size", "Background Colors", "Object Colors", "Sounds on/off"]
WindowSize=["400 x 400", "600 x 600", "800 x 800"]
BackgroundColors=["Red", "Green", "Blue", "Purple", "White", "Black", "Orange"]
ObjectColors=["Red", "Green", "Blue", "Purple", "White", "Black", "Orange"]
SoundsOnOff=["Sounds On", "Sounds Off"]
#Instructions=[""]
#Level1=[""]
#Level2[""]
#Scoreboard[""]


#global variables
colors = {'red':(150,0,0),'green':(0,200,0), 'blue':(0,0,255), 'purple':(150,0,150), 'white':(255,255,255), 'black':(0,0,0), 'orange':(255,155,0)}
WHITE=colors.get('white')
BLACK=colors.get('black')
GREEN=colors.get('green')
ORANGE=colors.get('orange')

counter=1

WIDTH=800
HEIGHT=800
wbox=30
hbox=30
x=70
y=150
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Main Menu")
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
    win.fill(WHITE)
    pygame.display.update
win.fill(WHITE)
display_Title("Main Menu",40)
Menu_function(MainMenuMessages, 150)

# if xp>x and xp<x+wbox and yp>y and yp<245:
#     create_NewWindow("Screen Size")
#     display_Title("Instructions",40)
# if xp>=70 and xp<x+wbox and yp>250 and yp<=275:
#     create_NewWindow("BackgroundColors")
#     display_Title("Level 1",40)
# if xp>=70 and xp<x+wbox and yp>350 and yp<375:
#     create_NewWindow("Object Colors")
#     display_Title("Level 2",40)
# if xp>=x and xp<x+wbox and yp>450  and yp<475:
#     create_NewWindow("Sounds on/off")
#     display_Title("Setttings",40)
# if xp>=x and xp<x+wbox and yp>550  and yp<575:
#     create_NewWindow("Back")
#     display_Title("Scoreboard",40)


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
                        win.fill(WHITE)
                        display_Title("Instructions",40)
                        display_Title("BACK",HEIGHT-100)
                        currentDisplay=DISPLAY_INSTRUCTIONS
                        myFile=open('instructions.txt','r')
                        yi=150
                        for line in myFile.readlines():
                            text=MENU_FONT.render(line, 1, BLACK)
                            win.blit(text, (40,yi))
                            pygame.display.update()
                            pygame.time.delay(100)
                            yi+=50
                        myFile.close()
                        if xp >355 and xp<460 and yp>745 and yp<795:
                            xp = 0
                            yp = 0
#                           Menu_back
                            DISPLAY_MAIN_MENU=True
                            DISPLAY_INSTRUCTIONS=False
                    if xp>=70 and xp<x+wbox and yp>250 and yp<=275:
                        xp = 0
                        yp = 0
                        create_NewWindow("Level 1")
                        win.fill(WHITE)
                        display_Title("Level 1",40)
                        display_Title("BACK",HEIGHT-100)                 
                        currentDisplay=DISPLAY_LEVEL_1
                    if xp>=70 and xp<x+wbox and yp>350 and yp<375:
                        xp = 0
                        yp = 0
                        create_NewWindow("Level 2")
                        win.fill(WHITE)
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
                        create_NewWindow("Scoreboard")
                        win.fill(WHITE)
                        display_Title("Scoreboard",40)
                        display_Title("BACK",HEIGHT-100)
                        currentDisplay=DISPLAY_SCOREBOARD
                    if xp>=x and xp<x+wbox and yp>650  and yp<675:
                        xp = 0
                        yp = 0
                        #update your score file
                        run=False
                if currentDisplay==DISPLAY_INSTRUCTIONS:
                    if xp>=WIDTH/2-40 and xp<WIDTH/2+50 and yp>HEIGHT-100 and yp<HEIGHT-50:
                        xp = 0
                        yp = 0
                        win.fill(WHITE)
                        display_Title("Main Menu",40)
                        Menu_function(MainMenuMessages, 150)
                        pygame.display.set_caption("Main Menu")
                        currentDisplay=DISPLAY_MAIN_MENU

                if currentDisplay==DISPLAY_LEVEL_1:
                    if xp>=WIDTH/2-40 and xp<WIDTH/2+50 and yp>HEIGHT-100 and yp<HEIGHT-50:
                        xp = 0
                        yp = 0
                        win.fill(WHITE)
                        display_Title("Main Menu",40)
                        Menu_function(MainMenuMessages, 150)
                        pygame.display.set_caption("Main Menu")
                        currentDisplay=DISPLAY_MAIN_MENU
                        
                if currentDisplay==DISPLAY_LEVEL_2:
                    if xp>=WIDTH/2-40 and xp<WIDTH/2+50 and yp>HEIGHT-100 and yp<HEIGHT-50:
                        xp = 0
                        yp = 0
                        win.fill(WHITE)
                        display_Title("Main Menu",40)
                        Menu_function(MainMenuMessages, 150)
                        pygame.display.set_caption("Main Menu")
                        currentDisplay=DISPLAY_MAIN_MENU

                if currentDisplay==DISPLAY_SETTINGS:
                    if xp>=WIDTH/2-40 and xp<WIDTH/2+50 and yp>HEIGHT-100 and yp<HEIGHT-50:
                        xp = 0
                        yp = 0
                        win.fill(WHITE)
                        display_Title("Main Menu",40)
                        Menu_function(MainMenuMessages, 150)
                        pygame.display.set_caption("Main Menu")
                        currentDisplay=DISPLAY_MAIN_MENU

                if currentDisplay==DISPLAY_SCOREBOARD:
                    if xp>=WIDTH/2-40 and xp<WIDTH/2+50 and yp>HEIGHT-100 and yp<HEIGHT-50:
                        xp = 0
                        yp = 0
                        win.fill(WHITE)
                        display_Title("Main Menu",40)
                        Menu_function(MainMenuMessages, 150)
                        pygame.display.set_caption("Main Menu")
                        currentDisplay=DISPLAY_MAIN_MENU              

                if currentDisplay==DISPLAY_SETTINGS:
                    if xp>x and xp<x+wbox and yp>y and yp<245:
                        xp = 0
                        yp = 0
                        win.fill(WHITE)
                        display_Title("Window Settings",40)
                        display_Title("BACK",HEIGHT-100)
                        Menu_function(WindowSize, 150)
                        pygame.display.set_caption("Window Settings")
                        currentDisplay=DISPLAY_WINDOW_SIZE

                if currentDisplay==DISPLAY_WINDOW_SIZE:
                    if xp>=WIDTH/2-40 and xp<WIDTH/2+50 and yp>HEIGHT-100 and yp<HEIGHT-50:
                        xp = 0
                        yp = 0
                        win.fill(WHITE)
                        display_Title("Settings",40)
                        display_Title("BACK",HEIGHT-100)
                        Menu_function(Settings,150)
                        pygame.display.set_caption("Settings")
                        currentDisplay=DISPLAY_SETTINGS  

                if currentDisplay==DISPLAY_SETTINGS:
                    if xp>=70 and xp<x+wbox and yp>250 and yp<=275:
                        xp = 0
                        yp = 0
                        win.fill(WHITE)
                        display_Title("Background Colors",40)
                        display_Title("BACK",HEIGHT-100)
                        Menu_function(BackgroundColors, 150)
                        pygame.display.set_caption("Background Colors")
                        currentDisplay=DISPLAY_SETTINGS_BACKGROUND_COLOR
            
                if currentDisplay==DISPLAY_SETTINGS_BACKGROUND_COLOR:
                    if xp>=WIDTH/2-40 and xp<WIDTH/2+50 and yp>HEIGHT-100 and yp<HEIGHT-50:
                        xp = 0
                        yp = 0
                        win.fill(WHITE)
                        display_Title("Settings",40)
                        display_Title("BACK",HEIGHT-100)
                        Menu_function(Settings,150)
                        pygame.display.set_caption("Settings")
                        currentDisplay=DISPLAY_SETTINGS

                if currentDisplay==DISPLAY_SETTINGS:
                    if xp>=70 and xp<x+wbox and yp>350 and yp<375:
                        xp = 0
                        yp = 0
                        win.fill(WHITE)
                        display_Title("Object Colors",40)
                        display_Title("BACK",HEIGHT-100)
                        Menu_function(ObjectColors, 150)
                        pygame.display.set_caption("Object Colors")
                        currentDisplay=DISPLAY_OBJECT_COLORS
                
                if currentDisplay==DISPLAY_OBJECT_COLORS:
                    if xp>=WIDTH/2-40 and xp<WIDTH/2+50 and yp>HEIGHT-100 and yp<HEIGHT-50:
                        xp = 0
                        yp = 0
                        win.fill(WHITE)
                        display_Title("Settings",40)
                        display_Title("BACK",HEIGHT-100)
                        Menu_function(Settings,150)
                        pygame.display.set_caption("Settings")
                        currentDisplay=DISPLAY_SETTINGS

                if currentDisplay==DISPLAY_SETTINGS:
                    if xp>=x and xp<x+wbox and yp>450  and yp<475:
                        xp = 0
                        yp = 0
                        win.fill(WHITE)
                        display_Title("Sounds On/Off",40)
                        display_Title("BACK",HEIGHT-100)
                        Menu_function(SoundsOnOff, 150)
                        pygame.display.set_caption("Sounds On/Off")
                        currentDisplay=DISPLAY_SOUNDS_ON_OFF

                if currentDisplay==DISPLAY_SOUNDS_ON_OFF:
                    if xp>=WIDTH/2-40 and xp<WIDTH/2+50 and yp>HEIGHT-100 and yp<HEIGHT-50:
                        xp = 0
                        yp = 0
                        win.fill(WHITE)
                        display_Title("Settings",40)
                        display_Title("BACK",HEIGHT-100)
                        Menu_function(Settings,150)
                        pygame.display.set_caption("Settings")
                        currentDisplay=DISPLAY_SETTINGS


    #win.fill((0,0,0))
    #display_Title("Yes")
    #win.fill((0,0,0))
    #py.time.delay(200)
pygame.quit()