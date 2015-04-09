__author__ = 'Toby'

import pygame

pygame.init()

#TODO: Implement auto detecting / auto scaling monitor thing.
displayWidth = 800
displayHeight = 600

# Declares the screen size and makes it fullscreen.
screen = pygame.display.set_mode((displayWidth, displayHeight), pygame.FULLSCREEN)

pygame.display.set_caption("Graphical Slot Machine")

def getDisplaySize():
    pass
