import pygame

import random

import net.Toby.GSM.Gamemodes as Gamemodes

from net.Toby.GSM.Display import Display
from net.Toby.GSM.Util import ResourceLoader
from net.Toby.GSM.Util import ImageTransformer

pygame.init()

ResourceLoader = ResourceLoader.ResourceLoader()
ImageTransformer = ImageTransformer.imageTransformer()
Gamemodes = Gamemodes.Gamemodes()


class ImageRenderer():

    def renderGameImages(self):
        if Gamemodes.gamemode == "Debug":
            ImageTransformer.imageScaler()
        else:
            Display.screen.blit(ResourceLoader.background, (0, 0))
            pygame.draw.rect(Display.screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                             (120, 285, 385, 75))
            Display.screen.blit(ResourceLoader.imgOne, (600, 130))
            Display.screen.blit(ResourceLoader.imgTwo, (600, 230))
            Display.screen.blit(ResourceLoader.imgThree, (600, 330))
            Display.screen.blit(ResourceLoader.imgFour, (600, 430))