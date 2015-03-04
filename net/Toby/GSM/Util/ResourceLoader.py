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

        self.loseMusic = "Assets//2SAD4ME.mp3"
        self.defeatMusic = pygame.mixer.music.load(self.loseMusic)

        # self.winMusic = "Assets//OBAT.mp3"
        # self.congratulations = pygame.mixer.music.load(self.winMusic)