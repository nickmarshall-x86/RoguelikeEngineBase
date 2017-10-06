from controllerBase import ControllerBase
import pygame

import constants as C
import Events

class DungeonViewController(ControllerBase):
    def __init__(self, mediator, configuration):
        super(DungeonViewController, self).__init__("DungeonViewController", mediator, configuration)
        self.Window = None

    def SetWindow(self, window):
        self.Window = window