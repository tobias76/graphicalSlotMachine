__author__ = 'Toby Reed'

import random
import sys

import net.Toby.GSM.Display.Display as Display
import net.Toby.GSM.Util.ResourceLoader as ResourceLoader
import net.Toby.GSM.Util.Colours as Colour

verMinor = sys.version_info.minor

ResourceLoader = ResourceLoader.ResourceLoader()

class FontRenderer:
    def __init__(self):
        self.message = ""

    #TODO: Antialias my fonts.
    def versionFourSplashRenderer(self):
        if verMinor == 4:
                ResourceLoader.font.render_to(Display.screen, (20, 20), "Toby's Graphical Slot Machine:",
                                              Colour.Blue, None,
                                              rotation=0,
                                              size=48)
                ResourceLoader.font.render_to(Display.screen, (20, 80), "GOTY Edition. Pegi 420",
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

    def versionThreeSplashRender(self):
                ResourceLoader.font.render_to(Display.screen, (20, 20), "Toby's Graphical Slot Machine:",
                                              Colour.Blue, None,
                                              rotation=0,
                                              ptsize=48)
                ResourceLoader.font.render_to(Display.screen, (20, 80), "GOTY Edition. Pegi 420",
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

