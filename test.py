import pygame
from playSounds import sounds

pygame.init()

pygame.display.set_caption('Whack a Fire!')
window_surface = pygame.display.set_mode((1600, 1200))

background = pygame.Surface((1600, 1200))

is_running = True

#Import Images
houseT = pygame.image.load("Assets\\HouseT.png").convert_alpha()
map = pygame.image.load("Assets\\EmptyMap.png").convert_alpha()

#starts to play the background music
sounds.playBG()

#start of game loop
while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        

    window_surface.blit(map, (0, 0))
    locations = []
    x,y = 20, 20
    for _ in range(4):
        for i in range(9):
            window_surface.blit(houseT, (x, y))
            locations.append((x, y))
            x+=175
        x = 20
        y+=320

    pygame.display.update()


