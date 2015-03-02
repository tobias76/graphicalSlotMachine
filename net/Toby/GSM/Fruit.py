__author__ = 'Toby'

import pygame

pygame.init()


class Fruit(pygame.sprite.Sprite):
    def __init__(self, reelGroup, reel, ID):
        pygame.sprite.Sprite.__init__(self)
        self.reelGroup = reelGroup
        self.ID = ID
        self.reel = reel

        if self.ID == 1:
            self.picture = "Chris1.png"  # TODO: Add Image
        if self.ID == 2:
            self.picture = "Chris2.png"  # TODO: Add Image
        if self.ID == 3:
            self.picture = "Chris3.png"  # TODO: Add Image
        if self.ID == 4:
            self.picture = "Chris4.jpg"  # TODO: Add Image

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