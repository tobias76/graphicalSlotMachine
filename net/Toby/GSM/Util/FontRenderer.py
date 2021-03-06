__author__ = 'Toby Reed'

import pygame

import random
import sys

import net.Toby.GSM.Display.Display as Display
import net.Toby.GSM.Util.ResourceLoader as ResourceLoader
import net.Toby.GSM.Util.Colours as Colour
import net.Toby.GSM.GlobalVariables as GlobalVariables

pygame.init()

verMinor = GlobalVariables.verMinor

ResourceLoader = ResourceLoader.ResourceLoader()


class FontRenderer:
    def __init__(self):
        self.message = ""

    # Any version four renderer uses size instead of ptsize
    def versionFourSplashRenderer(self):
        if verMinor == 4:
                ResourceLoader.font.render_to(Display.screen, (20, 20), "Weymouth College Slot Machine",
                                              (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                                               , None, rotation=0, size=48)
                ResourceLoader.font.render_to(Display.screen, (20, 80), "Snow Gaming",
                                              (random.randint(0, 255), random.randint(0, 255),
                                               random.randint(0, 255), 255), None,
                                              rotation=0,
                                              size=48)
                ResourceLoader.font.render_to(Display.screen, (20, 400), 'Press J to start a new game',
                                              (random.randint(0, 255), random.randint(0, 255),
                                               random.randint(0, 255), 255), None,
                                               rotation=0,
                                               size=36)
                ResourceLoader.font.render_to(Display.screen, (20, 450),
                                              'You should also insert a new credit by pressing F',
                                              (random.randint(0, 255), random.randint(0, 255),
                                               random.randint(0, 255), 255), None,
                                               rotation=0,
                                               size=36)

    # Any version four renderer uses ptsize instead of size
    def versionThreeSplashRender(self):
                ResourceLoader.font.render_to(Display.screen, (20, 20), "Weymouth College Slot Machine",
                                              Colour.Blue, None,
                                              rotation=0,
                                              ptsize=48)
                ResourceLoader.font.render_to(Display.screen, (20, 80), "Snow Gaming",
                                              (random.randint(0, 255), random.randint(0, 255),
                                               random.randint(0, 255), 255), None, rotation=0,
                                              ptsize=48)
                ResourceLoader.font.render_to(Display.screen, (20, 400), 'Press J to start a new game',
                                              (random.randint(0, 255), random.randint(0, 255),
                                               random.randint(0, 255), 255), None, rotation=0,

                                              ptsize=36)
                ResourceLoader.font.render_to(Display.screen, (20, 450),
                                              'You should also insert a new credit by pressing F',
                                              (random.randint(0, 255), random.randint(0, 255),
                                               random.randint(0, 255), 255), None, rotation=0,
                                              ptsize=36)

    def versionFourGameRenderer(self):
                ResourceLoader.font.render_to(Display.screen, (680, 130), "1",
                                              (random.randint(0, 255), random.randint(0, 255),
                                               random.randint(0, 255), 255), None, rotation=0,
                                               size=48)
                ResourceLoader.font.render_to(Display.screen, (680, 230), "3",
                                              (random.randint(0, 255), random.randint(0, 255),
                                               random.randint(0, 255), 255), None, rotation=0,
                                               size=48)
                ResourceLoader.font.render_to(Display.screen, (680, 330), "5",
                                              (random.randint(0, 255), random.randint(0, 255),
                                               random.randint(0, 255), 255), None, rotation=0,
                                               size=48)
                ResourceLoader.font.render_to(Display.screen, (680, 430), "10",
                                              (random.randint(0, 255), random.randint(0, 255),
                                               random.randint(0, 255), 255), None, rotation=0,
                                               size=48)


    def versionThreeGameRenderer(self):
                ResourceLoader.font.render_to(Display.screen, (680, 130), "1",
                                              (random.randint(0, 255), random.randint(0, 255),
                                               random.randint(0, 255), 255), None, rotation=0,
                                              ptsize=48)
                ResourceLoader.font.render_to(Display.screen, (680, 230), "3",
                                              (random.randint(0, 255), random.randint(0, 255),
                                               random.randint(0, 255), 255), None, rotation=0,
                                              ptsize=48)
                ResourceLoader.font.render_to(Display.screen, (680, 330), "5",
                                              (random.randint(0, 255), random.randint(0, 255),
                                               random.randint(0, 255), 255), None, rotation=0,
                                              ptsize=48)
                ResourceLoader.font.render_to(Display.screen, (680, 430), "10",
                                              (random.randint(0, 255), random.randint(0, 255),
                                               random.randint(0, 255), 255), None, rotation=0,
                                              ptsize=48)

    def versionFourAttractRenderer(self):
        #TODO: Center this.
        ResourceLoader.font.render_to(Display.screen, (random.randint(0, 800),random.randint(0, 600)), "Play again! its free!",
                                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255), None, rotation=0, size=48)


    def versionThreeAttractRenderer(self):
        #TODO: Center this.
        ResourceLoader.font.render_to(Display.screen, (random.randint(0, 800),random.randint(0, 600)), "Play again! its free!",
                                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 255), None, rotation=0, ptsize=48)
