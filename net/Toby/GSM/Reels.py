__author__ = 'Toby Reed'

import pygame

from net.Toby.GSM.Display import Display as Display

pygame.init()


class Reel(pygame.sprite.Sprite):
    def __init__(self, reelgroup, reelnumber):
        self.reelGroup = reelgroup

        self.reelnumber = reelnumber
        self.reelList = [0, 1, 2, 3, 4, 5]
        self.reelMove = 1
        self.reelNudge = 0
        self.stopTime = (240 + (self.reelnumber * 60))

    def stopReel(self):
        self.reelMove = 0

    def nudgeReel(self):
        self.reelMove = 1
        self.reelNudge = 1

    def startReel(self):
        self.reelMove = 1
        self.stopTime = (240 + (self.reelnumber * 60))

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
