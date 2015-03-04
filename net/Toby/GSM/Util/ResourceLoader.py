__author__ = '338111'

import pygame

import pygame.mixer

pygame.init()
pygame.mixer.init()


class ResourceLoader():
    def __init__(self):
        self.bg = pygame.image.load("Assets//Background.jpg")
        self.chris1 = "Assets//Chris1.png"
        self.chris2 = "Assets//Chris2.png"
        self.chris3 = "Assets//Chris3.png"
        self.chris4 = "Assets//Chris4.jpg"

        self.chr1 = pygame.image.load(self.chris1)
        self.chr2 = pygame.image.load(self.chris2)
        self.chr3 = pygame.image.load(self.chris3)
        self.chr4 = pygame.image.load(self.chris4)

        # Fonts
        self.font = pygame.freetype.Font("Assets//sans.ttf")

        # Sounds
        self.winMusic = pygame.mixer.Sound("Assets//OBAT.ogg")

        self.loseMusic = pygame.mixer.Sound("Assets//2SAD4ME.ogg")