__author__ = 'MC Ride'

import pygame
from pygame.locals import *
import pygame.freetype

import net.Toby.GSM.Display.Display as Display
import net.Toby.GSM.Util.FPS as FPS
import net.Toby.GSM.Fruit as Fruit
import net.Toby.GSM.Reels as Reels
import net.Toby.GSM.Machine as Machines

import sys
import random

verMaj = sys.version_info.major
verMinor = sys.version_info.minor
verMicro = sys.version_info.micro

pygame.init()

FPSClock = FPS.fpsClock

# Load Images
bg = pygame.image.load("Background.jpg")
chr1 = pygame.image.load("Chris1.png")
chr2 = pygame.image.load("Chris2.png")
chr3 = pygame.image.load("Chris3.png")
chr4 = pygame.image.load("Chris4.jpg")

reelGroup1 = pygame.sprite.Group()
reelGroup2 = pygame.sprite.Group()
reelGroup3 = pygame.sprite.Group()

reel1 = Reels.Reel(reelGroup1, 1)
reel2 = Reels.Reel(reelGroup2, 2)
reel3 = Reels.Reel(reelGroup3, 3)

# Load Fonts
font = pygame.freetype.Font("sans.ttf")


class fruitMachine():
    def __init__(self):
        self.credits = 0
        self.counter = 0
        self.fruitlist = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.end = 0
        self.message = ""
        self.fruitMachine()

    def fruitMachine(self):
            while self.credits > 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                self.keys = pygame.key.get_pressed()
                if self.keys[K_f] and reel1.reelMove == reel2.reelMove == reel3.reelMove == 0:
                    self.credits -= 1
                    self.counter = 9
                    self.end = 0
                    self.message = ""

                if verMinor == 4:
                    Display.screen.blit(bg, (0, 0))
                    pygame.draw.rect(Display.screen, (255, 0, 0), (120, 285, 385, 75))
                    Display.screen.blit(chr1, (600, 130))
                    font.render_to(Display.screen, (680,130), "1", (random.randint(0,255),random.randint(0, 255) ,
                                                                    random.randint(0,255),255), None, rotation=0, size=48)
                    Display.screen.blit(chr2, (600, 230))
                    font.render_to(Display.screen, (680,230), "3", (random.randint(0,255),random.randint(0, 255) ,
                                                                    random.randint(0,255),255), None, rotation=0, size=48)
                    Display.screen.blit(chr3, (600, 330))
                    font.render_to(Display.screen, (680,330), "5", (random.randint(0,255),random.randint(0, 255),
                                                                    random.randint(0,255),255), None, rotation=0, size=48)
                    Display.screen.blit(chr4, (600, 430))
                    font.render_to(Display.screen, (680,430), "10", (random.randint(0,255),random.randint(0, 255) ,
                                                                     random.randint(0,255),255), None, rotation=0, size=48)
                elif verMinor == 3:
                    Display.screen.blit(bg, (0, 0))
                    pygame.draw.rect(Display.screen, (255, 0, 0), (120, 285, 385, 75))
                    Display.screen.blit(chr1, (600, 130))
                    font.render_to(Display.screen, (680,130), "1", (random.randint(0,255),random.randint(0,255),
                                                                    random.randint(0,255),255), None, rotation=0,
                                   ptsize =48)
                    Display.screen.blit(chr2, (600, 230))
                    font.render_to(Display.screen, (680,230), "3", (random.randint(0,255),random.randint(0,255),
                                                                    random.randint(0,255),255), None, rotation=0,
                                   ptsize=48)
                    Display.screen.blit(chr3, (600, 330))
                    font.render_to(Display.screen, (680, 330), "5", (random.randint(0, 255), random.randint(0,255),
                                                                     random.randint(0, 255), 255), None, rotation=0,
                                   ptsize=48)
                    Display.screen.blit(chr4, (600, 430))
                    font.render_to(Display.screen, (680, 430), "10", (random.randint(0, 255), random.randint(0, 255),
                                                                      random.randint(0, 255), 255), None, rotation=0,
                                   size=48)

                self.counter += 1
                if self.counter == 10:
                    if reel1.reelMove == 1 and (reel1.stopTime) % 10:
                        chris = Fruit.Fruit(reelGroup1, 1, random.randint(1,4))
                        del self.fruitlist[0][0]
                        self.fruitlist[0].append(chris.ID)
                    if reel1.reelMove == 2 and (reel2.stopTime) % 10:
                        chris = Fruit.Fruit(reelGroup2, 2, random.randint(1,4))
                        del self.fruitlist[1][0]
                        self.fruitlist[1].append(chris.ID)
                    if reel1.reelMove == 3 and (reel3.stopTime) % 10:
                        chris = Fruit.Fruit(reelGroup3, 3, random.randint(1,4))
                        del self.fruitlist[2][0]
                        self.fruitlist[2].append(chris.ID)
                    self.counter = 0
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
                    else:
                        self.message = "Bitch please, you must be smokin' rocks."
                    self.end = 1

                reel1.draw()
                reel2.draw()
                reel3.draw()

                font.render_to(Display.screen, (5, 550), self.message, (random.randint(0, 255), random.randint(0 , 255), random.randint(0, 255),255),
                               None, rotation=0, size=42)
                font.render_to(Display.screen, (5, 5), ("Credits: " + str(self.credits)), (random.randint(0, 255),
                                                                                          random.randint(0, 255), random.randint(0, 255), 255), None, rotation=0, size = 72)

                FPS.fpsClock.tick(FPS.fps)
                pygame.display.update()

            while self.credits == 0:
                #print("Please enter a credit.")
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                self.keys = pygame.key.get_pressed()
                if self.keys[K_j]:
                    self.credits = 10
                    print(self.credits)
            self.fruitMachine()

fruity = fruitMachine()
