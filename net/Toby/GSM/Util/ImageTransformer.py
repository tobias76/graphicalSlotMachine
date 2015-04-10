__author__ = 'Toby'

import pygame

import net.Toby.GSM.Util.ResourceLoader as ResourceLoader
import net.Toby.GSM.Display.Display as Display

pygame.init()

ResourceLoader = ResourceLoader.ResourceLoader

#TODO: Make this more efficient

class imageTransformer():
    def __init__(self):

        self.displayHeight = Display.displayHeight
        self.displayWidth = Display.displayWidth

    def imageScaler(self):
        if self.displayHeight == 1366 & self.displayHeight == 720:
            ResourceLoader.bg = pygame.transform.scale(ResourceLoader.bg, (1366, 766))