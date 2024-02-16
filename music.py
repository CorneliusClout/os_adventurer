import pygame
import sys

pygame.init()


def intro_clip():
    # Instellingen
    muziek_path = "media/dial-up-modem-01.mp3"

    # Initialiseren van de mixer
    pygame.mixer.init()

    # Afspelen van de muziek
    pygame.mixer.music.load(muziek_path)
    pygame.mixer.music.play()

    # Wachten tot de muziek is afgelopen
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(30)

