import pygame
#from playSounds import sounds

def menu(screen):
    run = True

    image = pygame.image.load("Assets\\startMenuImg.png").convert_alpha()


    while run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                posx, posy = pos

                if (posx > 510 and posx < 1223) and (posy > 848 and posy < 1070):
                    run = False

            if event.type == pygame.QUIT:
                sounds.stopAllSounds()
                sys.exit()
                
        screen.blit(image, (0, 0))
        pygame.display.update()
