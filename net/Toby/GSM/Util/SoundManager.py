import random

import pygame
import pygame.mixer

pygame.init()


class SoundManager():
    def __init__(self):
        self.lossSounds = ["Assets//2SAD4ME.ogg", "Assets//2SED4AIRHORN.ogg"]  # list of sound objects
        self.winSounds = ["Assets//OBAT.ogg", "Assets//DSWYFD.ogg"]  # list of sound objects
        self.lossSound = pygame.mixer.Sound(self.lossSounds[0])
        self.winSound = pygame.mixer.Sound(self.winSounds[0])


    def playRandomLossSound(self):
        random.shuffle(self.lossSounds)
        self.lossSound = pygame.mixer.Sound(self.lossSounds[0])
        self.lossSound.play()


    def playRandomWinSound(self):
        random.shuffle(self.winSounds)
        self.winSound = pygame.mixer.Sound(self.winSounds[0])
        self.winSound.play()
