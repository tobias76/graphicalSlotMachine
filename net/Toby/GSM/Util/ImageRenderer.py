import pygame

from net.Toby.GSM.Display import Display
from net.Toby.GSM.Util import ResourceLoader
from net.Toby.GSM.Util import ImageTransformer

pygame.init()

ResourceLoader = ResourceLoader.ResourceLoader()
ImageTransformer = ImageTransformer.imageTransformer()

class ImageRenderer():

    def renderGameImages(self):
        ImageTransformer.imageScaler()
        Display.screen.blit(ResourceLoader.bg, (0, 0))
        pygame.draw.rect(Display.screen, (255, 0, 0), (120, 285, 385, 75))
        Display.screen.blit(ResourceLoader.imgOne, (600, 130))
        Display.screen.blit(ResourceLoader.imgTwo, (600, 230))
        Display.screen.blit(ResourceLoader.imgThree, (600, 330))
        Display.screen.blit(ResourceLoader.imgFour, (600, 430))