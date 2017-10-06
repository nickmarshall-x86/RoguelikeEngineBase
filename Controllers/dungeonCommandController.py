from controllerBase import ControllerBase
import Events
import constants as C
import pygame

class DungeonCommandController(ControllerBase):
    def __init__(self, mediator, configuration):
        super(DungeonCommandController, self).__init__("DungeonCommandController", mediator, configuration)
        self.MouseState = C.INPUTSTATE_OPEN

    def ProcessKeyboardEvent(self, event):
        if event.EventType == C.INPUTEVENT_KEYDOWN:
            if event.Key == pygame.K_ESCAPE:
                super(DungeonCommandController, self).Post(Events.QuitEvent())

    def ProcessMouseEvent(self, event):
        pass

    def Notify(self, event):
        if isinstance(event, Events.KeyboardInputEvent):
            self.ProcessKeyboardEvent(event)
        if isinstance(event, Events.MouseInputEvent):
            self.ProcessMouseEvent(event)