import pygame, sys
from playSounds import sounds
from startMenu import *
pygame.init()

window_surface = pygame.display.set_mode((1600, 1200))

alt = True

sounds.playBG()

menu(window_surface)
image = pygame.image.load("Assets\\emptyMap.png").convert_alpha()

window_surface.blit(image, (0, 0))
pygame.display.update()
        
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            sounds.playFireOut()

        if event.type == pygame.KEYDOWN:
            if alt:
                sounds.playWomanScream()
                alt = False
            else:
                sounds.playManScream()
                alt = True
        
        if event.type == pygame.QUIT:
            
            sounds.stopAllSounds()
            
            sys.exit()
