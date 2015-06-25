__author__ = 'Toby Reed'

import random

import pygame
import pygame.mixer

pygame.init()


class SoundManager():
    def __init__(self):
        self.lossSounds = ["net\Toby\GSM\Assets//2SAD4ME.ogg",
                           "net\Toby\GSM\Assets//2SED4AIRHORN.ogg"]  # list of sound objects
        self.winSounds = ['net\Toby\GSM\Assets//OBAT.ogg', 'net\Toby\GSM\Assets//DSWYFD.ogg']  # list of sound objects

        #This loads in the sound objects
        self.lossSound = pygame.mixer.Sound(self.lossSounds[0])
        self.winSound = pygame.mixer.Sound(self.winSounds[0])


    def playRandomLossSound(self):
        #This picks a random loss sound
        random.shuffle(self.lossSounds)
        #This loads the random sound
        self.lossSound = pygame.mixer.Sound(self.lossSounds[0])
        #This plays the sound
        self.lossSound.play()


    def playRandomWinSound(self):
        #This picks a random loss sound
        random.shuffle(self.winSounds)
        #This loads the random sound
        self.winSound = pygame.mixer.Sound(self.winSounds[0])
        #This plays the sound
        self.winSound.play()
