import pygame,sys

from playSounds import sounds
from startMenu import menu
from random import randint
import time



pygame.init()
pygame.font.init() # you have to call this at the start,
                   # if you want to use this module.
my_font = pygame.font.SysFont(None, 30)

pygame.display.set_caption('Whack a Fire!')
window_surface = pygame.display.set_mode((1600, 1200))

background = pygame.Surface((1600, 1200))

is_running = True

#Import Images
houseT = pygame.image.load("Assets\\HouseT.png").convert_alpha()
map = pygame.image.load("Assets\\EmptyMap.png").convert_alpha()


#starts to play the background music
sounds.playBG()
menu(window_surface)

burningHouse = pygame.image.load("Assets\\HouseF.png").convert_alpha()
gameover = pygame.image.load("Assets\\gameover.png").convert_alpha()
estate = [False]*36
counter = 0
difficulty = 100

#start of game loop
while is_running:
    if counter+1% 50 == 0:
        for i in range(len(estate)):
            estate[i] = False
    if estate.count(True) >= 36:
        is_running=False
    window_surface.blit(map, (0, 0))
    text_surface = my_font.render('Score : ' + str(counter), True, (0, 0, 0))
    window_surface.blit(text_surface, (750,0))
    houseFire = randint(0, 35)
    if randint(1, 10000) < difficulty:
        if randint(1, 100000) < 300:
            sounds.playWomanScream()
        estate[houseFire] = True
    rangex = []
    rangey = []
    locations = []
    x,y = 20, 20
    for j in range(4):
        for i in range(9):
            if not estate[(j*9)+i]:
                window_surface.blit(houseT, (x, y))
            else:
                window_surface.blit(burningHouse, (x, y))
            locations.append((x, y))
            rangex.append((x, x+151))
            rangey.append((y, y+192))
            x+=175

        x = 20
        y+=320
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            posx, posy = pos
            xfound = False
            yfound = False
            cx = 0
            for xcoord in rangex:
                lower, upper = xcoord
                if lower <= posx <= upper:
                    xfound = True
                    break
                if posx < lower:
                    break
                cx+=1
            cy = 0
            for ycoord in rangey:
                lower, upper = ycoord

                if lower <= posy <= upper:
                    yfound = True
                    break
                if posy < lower:
                    break
                cy+=1
            ycor = cy // 9

            if xfound and yfound and estate[cx+(9*ycor)]:
                estate[cx+(9*ycor)]= False
                counter+=1
                difficulty+=10
                sounds.playFireOut()


    pygame.display.update()
is_running=True
sounds.playManScream()
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    window_surface.blit(map, (0, 0))
    text_surface = my_font.render('Score : ' + str(counter), True, (0, 0, 0))
    window_surface.blit(text_surface, (750,0))
    window_surface.blit(gameover, (550, 300))
    pygame.display.update()

