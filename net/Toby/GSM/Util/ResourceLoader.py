__author__ = 'Toby Reed'

import pygame

import pygame.mixer

pygame.init()
pygame.mixer.init()


class ResourceLoader():
    def __init__(self):
        self.bg = pygame.image.load("net\Toby\GSM\Assets\Background.jpg")
        self.imageOne = "net\Toby\GSM\Assets\Totadile.png"
        self.imageTwo = "net\Toby\GSM\Assets\Togepi.png"
        self.imageThree = "net\Toby\GSM\Assets\Celebi.png"
        self.imageFour = "net\Toby\GSM\Assets\Pichu.png"

        self.imgOne = pygame.image.load(self.imageOne)
        self.imgTwo = pygame.image.load(self.imageTwo)
        self.imgThree = pygame.image.load(self.imageThree)
        self.imgFour = pygame.image.load(self.imageFour)

        # Fonts
        self.font = pygame.freetype.Font("net\Toby\GSM\Assets\\sans.ttf")

        # Sounds
        self.winMusic1 = pygame.mixer.Sound("net\Toby\GSM\Assets\OBAT.ogg")

        self.loseMusic = pygame.mixer.Sound("net\Toby\GSM\Assets/2SAD4ME.ogg")