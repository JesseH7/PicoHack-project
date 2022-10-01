import pygame


pygame.init()

pygame.display.set_caption('Whack a Fire!')
window_surface = pygame.display.set_mode((1600, 1200))

background = pygame.Surface((1600, 1200))
background.fill(pygame.Color('#000000'))

is_running = True
houseT = pygame.image.load("C:\Users\jh17g22\OneDrive - University of Southampton\Documents\GitHub\PicoHack-project\Assets\HouseT.png").convert()


while is_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    window_surface.blit(background, (0, 0))


    pygame.display.update()















