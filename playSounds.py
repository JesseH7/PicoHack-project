import pygame


class sounds:
    def __init__():
        pygame.mixer.init()
    def playBG():
        sound = pygame.mixer.Sound("Sounds\\BGmusic.mp3")
        channel = pygame.mixer.Channel(0)
        channel.play(sound, -1)
        channel.set_volume(0.3)
    def playGodlike():
        sound = pygame.mixer.Sound("Sounds\\godlike.mp3")
        channel = pygame.mixer.Channel(1)
        channel.play(sound)
        channel.set_volume(1)
    def playLegendary():
        sound = pygame.mixer.Sound("Sounds\\legendary.mp3")
        channel = pygame.mixer.Channel(2)
        channel.play(sound)
        channel.set_volume(1)
    def playUnstoppable():
        sound = pygame.mixer.Sound("Sounds\\unstoppable.mp3")
        channel = pygame.mixer.Channel(3)
        channel.play(sound)
        channel.set_volume(1)
    def playWomanScream():
        sound = pygame.mixer.Sound("Sounds\\screamWoman.mp3")
        channel = pygame.mixer.Channel(4)
        channel.play(sound)
        channel.set_volume(1)
    def playManScream():
        sound = pygame.mixer.Sound("Sounds\\screamMan.mp3")
        channel = pygame.mixer.Channel(5)
        channel.play(sound)
        channel.set_volume(0.5)

    def splash():
        sound = pygame.mixer.Sound("Sounds\\splash.mp3")
        channel = pygame.mixer.Channel(5)
        channel.play(sound)
        channel.set_volume(5)
    def playFireOut():
        #print(pygame.mixer.find_channel())
        sound = pygame.mixer.Sound("Sounds\\fireOut.mp3")
        try:
            pygame.mixer.find_channel().play(sound)
        except:
            pass
    def playMedium():
        sound = pygame.mixer.Sound("Sounds\\medium.mp3")
        channel = pygame.mixer.Channel(5)
        channel.play(sound)
        channel.set_volume(5)
    def playHard():
        sound = pygame.mixer.Sound("Sounds\\hard.mp3")
        channel = pygame.mixer.Channel(5)
        channel.play(sound)
        channel.set_volume(5)
    def playExtreme():
        sound = pygame.mixer.Sound("Sounds\\extreme.mp3")
        channel = pygame.mixer.Channel(5)
        channel.play(sound)
        channel.set_volume(5)
    def playFtNoise():
        sound = pygame.mixer.Sound("Sounds\\firetrucknoise.mp3")
        channel = pygame.mixer.Channel(5)
        channel.play(sound)
        channel.set_volume(2)
    def playManScream():
        sound = pygame.mixer.Sound("Sounds\\screamMan.mp3")
        channel = pygame.mixer.Channel(5)
        channel.play(sound)
        channel.set_volume(5)
        channel.set_volume(0.5)

    def stopAllSounds():
        pygame.mixer.quit()
