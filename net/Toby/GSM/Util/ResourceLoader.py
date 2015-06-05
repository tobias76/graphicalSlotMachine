__author__ = 'Toby Reed'

import pygame

import pygame.mixer

pygame.init()


class ResourceLoader():
    def __init__(self):
        #This section of code creates an object from the assets file location
        self.bg = "net\Toby\GSM\Assets\Background.jpg"
        self.imageOne = "net\Toby\GSM\Assets\Totadile.png"
        self.imageTwo = "net\Toby\GSM\Assets\Togepi.png"
        self.imageThree = "net\Toby\GSM\Assets\Celebi.png"
        self.imageFour = "net\Toby\GSM\Assets\Pichu.png"

        #This loads in images using their necessary object
        self.background = pygame.image.load(self.bg)
        self.imgOne = pygame.image.load(self.imageOne)
        self.imgTwo = pygame.image.load(self.imageTwo)
        self.imgThree = pygame.image.load(self.imageThree)
        self.imgFour = pygame.image.load(self.imageFour)

        # Fonts
        #This loads the ingame fonts
        self.font = pygame.freetype.Font("net\Toby\GSM\Assets\\sans.ttf")

        # Sounds
