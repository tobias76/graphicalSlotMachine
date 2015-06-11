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
import net.Toby.GSM.Reels as Reels

from net.Toby.GSM.Util import SoundManager as SoundManager
from net.Toby.GSM.Display import Display as Display
from net.Toby.GSM.Util import FontRenderer as FontRenderer
from net.Toby.GSM.Util import ImageRenderer as ImageRenderer
from net.Toby.GSM import GlobalVariables as GlobalVariables

pygame.init()

FPSClock = FPS.fpsClock

# Create a ResourceLoader object
ResourceLoader = ResourceLoader.ResourceLoader()

reelGroup1 = pygame.sprite.Group()
reelGroup2 = pygame.sprite.Group()
reelGroup3 = pygame.sprite.Group()

reel1 = Reels.Reel(reelGroup1, 1)
reel2 = Reels.Reel(reelGroup2, 2)
reel3 = Reels.Reel(reelGroup3, 3)

SoundManager = SoundManager.SoundManager()
FontRenderer = FontRenderer.FontRenderer()
ImageRenderer = ImageRenderer.ImageRenderer()


class fruitMachine():
    def __init__(self):
        self.credits = GlobalVariables.ingameCredits
        self.counter = 5
        self.fruitlist = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        self.end = False
        self.message = ""
        self.splash()

    def splash(self):
        while True:
            # The first two statements render the splash screen
            if GlobalVariables.verMinor == 4:
                FontRenderer.versionFourSplashRenderer()

            elif GlobalVariables.verMinor == 3:
                FontRenderer.versionThreeSplashRender()

            for event in pygame.event.get():
                # This sets up a quit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # This is a list of the keys pressed
            self.keys = pygame.key.get_pressed()
            # This says if you press J to start the slot machine
            if self.keys[K_j]:
                self.fruitMachine()
            # This sets escape to quit the game
            if self.keys[K_ESCAPE]:
                pygame.quit()
                sys.exit()
            # This ticks the fps clock and updates the display
            FPS.fpsClock.tick(FPS.fps)
            pygame.display.update()

    def fruitMachine(self):
        while self.credits > 0:
            # This sets up a quit event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # This is a list of the keys pressed
            self.keys = pygame.key.get_pressed()
            # This says that if you press F and the reels aren't moving to remove one credit and set them to the moving
            # state.
            if self.keys[K_f] and reel1.reelMove == reel2.reelMove == reel3.reelMove == False:
                self.credits -= 1
                self.counter = 5
                self.end = False
                # This starts the reels
                reel1.startReel()
                reel2.startReel()
                reel3.startReel()
                # This stops the sounds
                pygame.mixer.Sound.stop(SoundManager.lossSound)
                pygame.mixer.Sound.stop(SoundManager.winSound)
                # This sets the message to blank.
                self.message = ""

            if self.keys[K_ESCAPE]:
                pygame.quit()
                sys.exit(0)

            # This renders the game images
            ImageRenderer.renderGameImages()

            # These two render the game screen to the display
            if GlobalVariables.verMinor == 4:
                FontRenderer.versionFourGameRenderer()

            elif GlobalVariables.verMinor == 3:
                FontRenderer.versionThreeGameRenderer()

            # If the counter is more than or equal to ten it sets it to one, it then sets the reel to true, gets the
            # remainder of the stop time, chooses a random fruit, deletes the previous fruit and then add the new one
            # to the fruitlist.
            if self.counter >= 10:
                self.counter = 1
                if reel1.reelMove == True and reel1.stopTime % 10:
                    item = Fruit.Fruit(reelGroup1, 1, random.randint(1, 4))
                    del self.fruitlist[0][0]
                    self.fruitlist[0].append(item.ID)
                if reel2.reelMove == True and reel2.stopTime % 10:
                    item = Fruit.Fruit(reelGroup2, 2, random.randint(1, 4))
                    del self.fruitlist[1][0]
                    self.fruitlist[1].append(item.ID)
                if reel3.reelMove == True and reel3.stopTime % 10:
                    item = Fruit.Fruit(reelGroup3, 3, random.randint(1, 4))
                    del self.fruitlist[2][0]
                    self.fruitlist[2].append(item.ID)
            else:
                self.counter += 1
            # This piece of code update the reels if they're moving.
            if reel1.reelMove == True:
                reel1.update()
            if reel2.reelMove == True:
                reel2.update()
            if reel3.reelMove == True:
                reel3.update()
            # If the reels aren't moving and they are matching the game adds the correct amount of credits to the credit
            # total
            if reel1.reelMove == reel2.reelMove == reel3.reelMove == 0 and self.end == False:
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
                    # This plays a random win sound and sets the game to the end.
                    SoundManager.playRandomWinSound()
                    self.end = True
                # If they don't match it plays a loss sound and renders a message to the screen.
                else:
                    self.message = "You did not win this time, try again?"
                    SoundManager.playRandomLossSound()
                    self.end = True

            # This draws the reels to the screen.
            reelGroup1.draw(Display.screen)
            reelGroup2.draw(Display.screen)
            reelGroup3.draw(Display.screen)

            # These two statements render the games UI to the screen.
            if GlobalVariables.verMinor == 4:

                ResourceLoader.font.render_to(Display.screen, (5, 550), self.message,
                                              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),
                                               255),
                                              None, rotation=0, size=42)
                ResourceLoader.font.render_to(Display.screen, (5, 5), ("Credits: " + str(self.credits)),
                                              (random.randint(0, 255),
                                               random.randint(0, 255),
                                               random.randint(0, 255), 255),
                                              None, rotation=0, size=72)

            if GlobalVariables.verMinor == 3:

                ResourceLoader.font.render_to(Display.screen, (5, 550), self.message,
                                              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),
                                               255),
                                              None, rotation=0, ptsize=42)

                ResourceLoader.font.render_to(Display.screen, (5, 5), ("Credits: " + str(GlobalVariables.ingameCredits)),
                                              (random.randint(0, 255),
                                               random.randint(0, 255),
                                               random.randint(0, 255), 255),
                                              None, rotation=0, ptsize=72)

            FPS.fpsClock.tick(FPS.fps)
            pygame.display.update()

        if self.credits == 0:
            self.attract()

    def attract(self):
        while self.credits == 0:
            # These two render attract mode to the screen.
            if GlobalVariables.verMinor == 4:
                FontRenderer.versionFourAttractRenderer()
            elif GlobalVariables.verMinor == 3:
                FontRenderer.versionThreeAttractRenderer()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.keys[K_ESCAPE]:
                    pygame.quit()
                    sys.exit()

            self.keys = pygame.key.get_pressed()
            if self.keys[K_j]:
                self.credits = 1
                self.fruitMachine()
            FPSClock.tick(FPS.fps)
            pygame.display.update()
