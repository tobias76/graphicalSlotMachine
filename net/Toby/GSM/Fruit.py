__author__ = 'Toby Reed'

import pygame

import net.Toby.GSM.Util.ResourceLoader as ResourceLoader

pygame.init()

# Load Images
ResourceLoader = ResourceLoader.ResourceLoader()


class Fruit(pygame.sprite.Sprite):
    def __init__(self, reelGroup, reel, ID):
        pygame.sprite.Sprite.__init__(self)
        self.reelGroup = reelGroup
        self.ID = ID
        self.reel = reel

        if self.ID == 1:
            self.picture = ResourceLoader.chris1
        if self.ID == 2:
            self.picture = ResourceLoader.chris2
        if self.ID == 3:
            self.picture = ResourceLoader.chris3
        if self.ID == 4:
            self.picture = ResourceLoader.chris4

        self.image = pygame.image.load(self.picture).convert_alpha()
        self.location = ((self.reel * 155) - 30, 490)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.location
        self.speed = 8
        self.reelGroup.add(self)

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 110:
            self.kill()