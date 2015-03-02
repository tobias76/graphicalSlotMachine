__author__ = 'Toby'

import random

import pygame
import pygame.freetype
from pygame.locals import *

from net.Toby.GSM.Display import Display as Display
from net.Toby.GSM.Util import Colours as Colours
from net.Toby.GSM import Reels as Reels
import net.Toby.GSM.Fruit as Fruit


pygame.init()


class Machine():
    def __init__(self):
        self.credits = 10
        self.reset = 0
        self.start = "Start"
        self.font = "Read Todo"  # TODO: Add font
        self.fruitMachine()


    def spinReel(self):
        if Reels.reelMove[0] == 1:
            Reels.reel1_group.update()
        if Reels.reelMove[1] == 1:
            Reels.reel2_group.update()
        if Reels.reelMove[2] == 2:
            Reels.reel3_group.update()

        self.reset += 1

        if self.reset == 12:
            self.reset = 0
            if Reels.reelMove[2] == 1:
                del Reels.reel3_list[0]
                Reels.reel3_list.append(random.randint(1, 5))
                Fruit(Reels.reel3_group, 3, Reels.reel3_list[4])
            if Reels.reelMove[1] == 1:
                del Reels.reel2_list[0]
                Reels.reel2_list.append(random.randint(1, 5))
                Fruit(Reels.reel2_group, 2, Reels.reel2_list[4])
            if Reels.reelMove[0] == 1:
                Reels.reel1_list.append(random.randint(1, 5))
                Fruit(Reels.reel1_group, 1, Reels.reel1_list[4])

        Reels.reel1_group.draw(Display.screen)
        Reels.reel2_group.draw(Display.screen)
        Reels.reel3_group.draw(Display.screen)

    def stopReel(self):
        keys = pygame.key.get_pressed()
        if keys[K_RETURN]:
            Reels.reelMove[0] = 0
            Reels.reelMove[1] = 0
            Reels.reelMove[2] = 0

    def startReel(self):
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            Reels.reelMove[0] = 1
            Reels.reelMove[1] = 1
            Reels.reelMove[2] = 1

    def winnings(self):
        if Reels.reelMove[0] == Reels.reelMove[1] == Reels.reelMove[2] == 0:
            if Reels.reel1_list[2] == Reels.reel2_list[2] == Reels.reel3_list[2]:
                if Reels.reel1_list[2] == 1:
                    self.credits += 5
                    self.winning = 5
            if Reels.reel1_list[2] == 2:
                self.credits += 1
                self.winning = 1
            if Reels.reel1_list[2] == 3:
                self.credits += 3
                self.winning = 3
            if Reels.reel1_list[2] == 4:
                self.credits += 10
                self.winning = 10
            if Reels.reel1_list[2] == 5:
                pygame.quit()
                self.displayWinnings

    def displayWinnings(self):
        if Reels.reel1_list[2] == 4:
            self.font.render_to(Display.screen, (80, 60), ("Well done! You have won the max prize"), (Colours.Green),
                                rotation=0, ptsize=44)
        else:
            self.font.render_to(Display.screen, (80, 60), ("Your total winnings " + str(self.winning) + " credits"),
                                (Colours.Green), None, rotation=0, ptsize=44)