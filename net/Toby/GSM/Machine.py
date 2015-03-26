__author__ = 'Toby Reed'

import sys
import random

import pygame
import pygame.freetype
import pygame.mixer
from pygame.locals import *

import net.Toby.GSM.Util.FPS as FPS
import net.Toby.GSM.Fruit as Fruit
import net.Toby.GSM.Util.ResourceLoader as ResourceLoader

from net.Toby.GSM import Reels as Reels
from net.Toby.GSM.Util import SoundManager as SoundManager
from net.Toby.GSM.Display import Display as Display
from net.Toby.GSM.Util import FontRenderer as FontRenderer


verMaj = sys.version_info.major
verMinor = sys.version_info.minor
verMicro = sys.version_info.micro

pygame.init()

FPSClock = FPS.fpsClock

# Load Images
ResourceLoader = ResourceLoader.ResourceLoader()

reelGroup1 = pygame.sprite.Group()
reelGroup2 = pygame.sprite.Group()
reelGroup3 = pygame.sprite.Group()

reel1 = Reels.Reel(reelGroup1, 1)
reel2 = Reels.Reel(reelGroup2, 2)
reel3 = Reels.Reel(reelGroup3, 3)

SoundManager = SoundManager.SoundManager()
FontRenderer = FontRenderer.FontRenderer()


class fruitMachine():
    def __init__(self):
        self.credits = 10
        self.counter = 5
        self.fruitlist = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.end = 0
        self.message = ""
        self.splash()

    def splash(self):
        while True:

            if verMinor == 4:
                FontRenderer.versionFourSplashRenderer()

            elif verMinor == 3:
                FontRenderer.versionThreeSplashRender()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.keys = pygame.key.get_pressed()
            if self.keys[K_j]:
                self.fruitMachine()
            if self.keys[K_ESCAPE]:
                pygame.quit()
                sys.exit()
            FPS.fpsClock.tick(FPS.fps)
            pygame.display.update()

    def fruitMachine(self):
        while self.credits > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.keys = pygame.key.get_pressed()

            if self.keys[K_f] and reel1.reelMove == reel2.reelMove == reel3.reelMove == 0:
                self.credits -= 1
                self.counter = 5
                self.end = 0
                reel1.startReel()
                reel2.startReel()
                reel3.startReel()
                pygame.mixer.Sound.stop(SoundManager.lossSound)
                pygame.mixer.Sound.stop(SoundManager.winSound)
                self.message = ""
            if self.keys[K_ESCAPE]:
                pygame.quit()
                sys.exit(0)

            Display.screen.blit(ResourceLoader.bg, (0, 0))
            pygame.draw.rect(Display.screen, (255, 0, 0), (120, 285, 385, 75))
            Display.screen.blit(ResourceLoader.imgOne, (600, 130))
            Display.screen.blit(ResourceLoader.imgTwo, (600, 230))
            Display.screen.blit(ResourceLoader.imgThree, (600, 330))
            Display.screen.blit(ResourceLoader.imgFour, (600, 430))

            if verMinor == 4:
                FontRenderer.versionFourGameRenderer()

            elif verMinor == 3:
                FontRenderer.versionThreeGameRenderer()

            if self.counter >= 10:
                self.counter = 1
                if reel1.reelMove == 1 and reel1.stopTime % 10:
                    chris = Fruit.Fruit(reelGroup1, 1, random.randint(1, 4))
                    del self.fruitlist[0][0]
                    self.fruitlist[0].append(chris.ID)
                if reel2.reelMove == 1 and reel2.stopTime % 10:
                    chris = Fruit.Fruit(reelGroup2, 2, random.randint(1, 4))
                    del self.fruitlist[1][0]
                    self.fruitlist[1].append(chris.ID)
                if reel3.reelMove == 1 and reel3.stopTime % 10:
                    chris = Fruit.Fruit(reelGroup3, 3, random.randint(1, 4))
                    del self.fruitlist[2][0]
                    self.fruitlist[2].append(chris.ID)
            else:
                self.counter += 1
            if reel1.reelMove == 1:
                reel1.update()
            if reel2.reelMove == 1:
                reel2.update()
            if reel3.reelMove == 1:
                reel3.update()
            if reel1.reelMove == reel2.reelMove == reel3.reelMove == 0 and self.end == 0:
                if self.fruitlist[0][2] == self.fruitlist[1][2] == self.fruitlist[2][2]:
                    self.message = "Congratulations, you have won 0/"
                    if self.fruitlist[0][2] == 1:
                        self.credits += 1
                    if self.fruitlist[0][2] == 2:
                        self.credits += 3
                    if self.fruitlist[0][2] == 3:
                        self.credits += 5
                    if self.fruitlist[0][2] == 4:
                        self.credits += 10
                    SoundManager.playRandomWinSound()
                    self.end = 1
                else:
                    self.message = "You did not win this time, try again?"
                    SoundManager.playRandomLossSound()
                    self.end = 1

            reelGroup1.draw(Display.screen)
            reelGroup2.draw(Display.screen)
            reelGroup3.draw(Display.screen)

            if verMinor == 4:

                ResourceLoader.font.render_to(Display.screen, (5, 550), self.message,
                                              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),
                                               255),
                                              None, rotation=0, size=42)
                ResourceLoader.font.render_to(Display.screen, (5, 5), ("Credits: " + str(self.credits)),
                                          (random.randint(0, 255),
                                           random.randint(0, 255),
                                           random.randint(0, 255), 255),
                                          None, rotation=0, size=72)


            if verMinor == 3:

                ResourceLoader.font.render_to(Display.screen, (5, 550), self.message,
                                              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),
                                               255),
                                              None, rotation=0, ptsize=42)

                ResourceLoader.font.render_to(Display.screen, (5, 5), ("Credits: " + str(self.credits)),
                                              (random.randint(0, 255),
                                               random.randint(0, 255),
                                               random.randint(0, 255), 255),
                                              None, rotation=0, ptsize=72)

            FPS.fpsClock.tick(FPS.fps)
            pygame.display.update()
        if self.credits == 0:
            self.attract()

    def attract(self):
        self.mc = pygame.image.load("Assets//mcride.png")
        Display.screen.blit(self.mc, (200, 100))
        pygame.display.update()
        while self.credits == 0:
            print("Please enter a credit.")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.keys[K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            self.keys = pygame.key.get_pressed()
            if self.keys[K_j]:
                self.credits = 10
                print(self.credits)
                self.fruitMachine()