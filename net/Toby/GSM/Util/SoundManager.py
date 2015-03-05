import random

import pygame
import pygame.mixer

class SoundManager:

    lossSounds = ["Assets//2SAD4ME.ogg", "Assets//2SED4AIRHORN.ogg"] # list of sound objects
    winSounds = ["Assets//OBAT.ogg", "Assets//DSWYFD.ogg"] # list of sound objects


def playRandomLossSound():
    winSound = random.choice(SoundManager.lossSounds)
    pygame.mixer.Sound(winSound).play()

def playRandomWinSound():
    sound = random.choice(SoundManager.winSounds)
    pygame.mixer.Sound(sound).play()
