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

        # Checks the fruits ID and sets the image based on the ID
        if self.ID == 1:
            self.picture = ResourceLoader.imageOne
        if self.ID == 2:
            self.picture = ResourceLoader.imageTwo
        if self.ID == 3:
            self.picture = ResourceLoader.imageThree
        if self.ID == 4:
            self.picture = ResourceLoader.imageFour

        self.image = pygame.image.load(self.picture).convert_alpha()
        # This sets the position on the screen
        self.location = ((self.reel * 155) - 30, 490)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.location
        #This sets the reel speed, set in pixel per second.
        self.speed = 8
        #Adds the fruit to a reel group
        self.reelGroup.add(self)

    def update(self):
        #This checks if the rect is less than or equal to the speed
        self.rect.y -= self.speed
        if self.rect.y < 110:
            self.kill()