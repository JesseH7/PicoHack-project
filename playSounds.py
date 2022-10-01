import pygame

class sounds:
    def __init__(self):
        pygame.mixer.init()
    def playBG():
        sound = pygame.mixer.Sound("Sounds\\BGmusic.mp3")
        channel = pygame.mixer.Channel(0)
        channel.play(sound, -1)
        channel.set_volume(0.3)
    def playFireOut():
        sound = pygame.mixer.Sound("Sounds\\fireOut.mp3")
        channel = pygame.mixer.Channel(1)
        channel.play(sound)
        channel.set_volume(1.5)
    def playWomanScream():
        sound = pygame.mixer.Sound("Sounds\\screamWoman.mp3")
        channel = pygame.mixer.Channel(2)
        channel.play(sound)
        channel.set_volume(1)
    def playManScream():
        sound = pygame.mixer.Sound("Sounds\\screamMan.mp3")
        channel = pygame.mixer.Channel(3)
        channel.play(sound)
        channel.set_volume(0.5)
    def stopAllSounds():
        pygame.mixer.quit()
