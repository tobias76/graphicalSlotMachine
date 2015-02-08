__author__ = 'Toby'

import pygame

from net.Toby.GSM import Reels

pygame.init()

class Fruit(pygame.sprite.Sprite):
    def __init__(self, reelGroup, reel, ID):
        pygame.sprite.Sprite.__init__(self)
        self.reelGroup = reelGroup
        self.ID = ID
        self.reel = reel

        if self.ID == 1:
            self.picture = "" #TODO: Add Image
        if self.ID == 2:
            self.picture = "" #TODO: Add Image
        if self.ID == 3:
            self.picture = "" #TODO: Add Image
        if self.ID == 4:
            self.picture = "" #TODO: Add Image

        self.image = pygame.image.load(self.picture).convert_alpha()
        self.location = ((self.reel * 155) - 30, 420)
        self.rect = self.image.get_rect()
        self.rect.topLeft = self.location
        self.speed = 12
        self.reelGroupAdd(self)

    def update(self):
        self.rect.y = self.speed
        if self.rect.y < 120:
            self.kill()