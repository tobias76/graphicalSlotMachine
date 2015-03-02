__author__ = 'Toby'

import random

import pygame

import net.Toby.GSM.Display.Display as Display

pygame.init()


class Reel(pygame.sprite.Sprite):
    def __init__(self, reelGroup, reelnumber):
        self.reelGroup = reelGroup

        self.reelList = [1, 2, 3, 4, 5]
        self.reelMove = 1
        self.reelNudge = 0
        self.stopTime = (240 + (60 * (random.randint(1, 6) + reelnumber)))

    def stopReel(self):
        self.reelMove = 0

    def nudgeReel(self):
        self.reelMove = 1
        self.reelNudge = 1

    def update(self):
        if self.stopTime > 0:
            self.stopTime -= 1
            self.reelGroup.update()
        else:
            self.stopReel()
        if self.reelNudge == 1:
            self.reelMove = 0

    def draw(self):
        self.reelGroup.draw(Display.screen)
