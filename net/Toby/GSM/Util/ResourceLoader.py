__author__ = 'Toby Reed'

import pygame

import pygame.mixer

pygame.init()
pygame.mixer.init()


class ResourceLoader():
    def __init__(self):
        self.bg = pygame.image.load("net\Toby\GSM\Assets\Background.jpg")
        self.imageOne = "net\Toby\GSM\Assets\Totadile.png"
        self.chris2 = "net\Toby\GSM\Assets\Chris2.png"
        self.chris3 = "net\Toby\GSM\Assets\Chris3.png"
        self.chris4 = "net\Toby\GSM\Assets\Chris4.jpg"

        self.imgOne = pygame.image.load(self.imageOne)
        self.chr2 = pygame.image.load(self.chris2)
        self.chr3 = pygame.image.load(self.chris3)
        self.chr4 = pygame.image.load(self.chris4)

        # Fonts
        self.font = pygame.freetype.Font("net\Toby\GSM\Assets\\sans.ttf")

        # Sounds
        self.winMusic1 = pygame.mixer.Sound("net\Toby\GSM\Assets\OBAT.ogg")

        self.loseMusic = pygame.mixer.Sound("net\Toby\GSM\Assets/2SAD4ME.ogg")