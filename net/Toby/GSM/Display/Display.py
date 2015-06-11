__author__ = 'Toby'

import pygame
import net.Toby.GSM.Gamemodes as Gamemodes

pygame.init()

Gamemodes = Gamemodes.Gamemodes()

# TODO: Implement auto scaling to monitor thing.

# If the gamemode = debug it sets the displayHeight and displayWidth to the size of the monitor, otherwise it is set t0
# 800x600
if Gamemodes.gamemode == "Debug":
    displayWidth = pygame.display.Info().current_w
    displayHeight = pygame.display.Info().current_h
else:
    displayWidth = 800
    displayHeight = 600

# Declares the screen size and makes it fullscreen.
screen = pygame.display.set_mode((displayWidth, displayHeight), pygame.FULLSCREEN)

# Sets the screens title.
pygame.display.set_caption("Weymouth College Slot Machine")
