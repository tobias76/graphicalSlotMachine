__author__ = 'Toby'

import pygame

import net.Toby.GSM.Util.ResourceLoader as ResourceLoader
import net.Toby.GSM.Display.Display as Display

pygame.init()

ResourceLoader = ResourceLoader.ResourceLoader

#TODO: Make this more efficient

class imageTransformer():
    def __init__(self):

        # This creates a local variable using the display class's display size variable
        self.displayHeight = Display.displayHeight
        self.displayWidth = Display.displayWidth

    # This feature is highly broken and unlikely to work when called, it checks for the screen size and scales the image
    # to the size needed to fill the screen.
    def imageScaler(self):
        if self.displayHeight != 800 & self.displayHeight != 600:
            ResourceLoader.bg = pygame.transform.scale(ResourceLoader.bg, (self.displayHeight, self.displayWidth))
            Display.screen.blit(ResourceLoader.bg, (0, 0))