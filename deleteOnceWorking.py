import pygame
from playSounds import sounds
pygame.init()

gameDisplay = pygame.display.set_mode((640, 480))

sounds.playBG()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
