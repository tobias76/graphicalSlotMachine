__author__ = 'Toby'

import pygame

pygame.init()

#TODO: Implement auto scaling to monitor thing.

displayWidth = pygame.display.Info().current_w
displayHeight = pygame.display.Info().current_h

# Declares the screen size and makes it fullscreen.
screen = pygame.display.set_mode((displayWidth, displayHeight), pygame.FULLSCREEN)

pygame.display.set_caption("Graphical Slot Machine")

def getDisplaySize():
    pass
