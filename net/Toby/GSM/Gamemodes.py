__author__ = 'Toby'

import pygame

import net.Toby.GSM.GlobalVariables as GlobalVariables

pygame.init()


class Gamemodes():
    def __init__(self):
        self.credits = GlobalVariables.ingameCredits
        #This allows me to work on different features without breaking the rest of the game
        self.gamemode = "Play"