import random

import pygame
import pygame.mixer

pygame.init()


class SoundManager():
    def __init__(self):
        self.lossSounds = ["net\Toby\GSM\Assets//2SAD4ME.ogg",
                           "net\Toby\GSM\Assets//2SED4AIRHORN.ogg"]  # list of sound objects
        self.winSounds = ["net\Toby\GSM\Assets//OBAT.ogg", "net\Toby\GSM\Assets//DSWYFD.ogg"]  # list of sound objects
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
