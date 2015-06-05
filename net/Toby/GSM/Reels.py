__author__ = 'Toby Reed'

import pygame

from net.Toby.GSM.Display import Display as Display

pygame.init()


class Reel(pygame.sprite.Sprite):
    def __init__(self, reelgroup, reelnumber):
        self.reelGroup = reelgroup

        self.reelnumber = reelnumber
        self.reelList = [0, 1, 2, 3, 4, 5]
        self.reelMove = True
        self.reelNudge = False
        self.stopTime = (240 + (self.reelnumber * 60))

    def stopReel(self):
        self.reelMove = False

    #TODO: Implement nudging
    def nudgeReel(self):
        self.reelMove = True
        self.reelNudge = 1

    def startReel(self):
        self.reelMove = True
        #This sets the stop time to the reel number times 60fps
        self.stopTime = (240 + (self.reelnumber * 60))

    def update(self):
        if self.stopTime > 0:
            self.stopTime -= 1
            self.reelGroup.update()
        else:
            self.stopReel()
        if self.reelNudge == True:
            self.reelMove = False

    def draw(self):
        self.reelGroup.draw(Display.screen)
