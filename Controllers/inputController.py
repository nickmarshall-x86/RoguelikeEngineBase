from controllerBase import ControllerBase
import pygame
import Events
import constants as C

# This class ONLY converts pygame events into mediated events  
# that way we can swap out handling controllers for each

class InputController(ControllerBase):
    def __init__(self, mediator, configuration):
        super(InputController, self).__init__("InputController", mediator, configuration)
        self.PyGameEventMappings = {
            pygame.MOUSEBUTTONDOWN: C.INPUTEVENT_MOUSEDOWN,
            pygame.MOUSEBUTTONUP: C.INPUTEVENT_MOUSEUP,
            pygame.MOUSEMOTION: C.INPUTEVENT_MOUSEMOVE,
            pygame.KEYDOWN: C.INPUTEVENT_KEYDOWN,
            pygame.KEYUP: C.INPUTEVENT_KEYUP
        }

    def ProcessPyGameEvent(self, pgEvent):
        if pgEvent.type in [pygame.KEYDOWN, pygame.KEYUP]:
            return Events.KeyboardInputEvent(self.PyGameEventMappings[pgEvent.type], pgEvent.key)
        
        # If MOUSEMOTION floods the inputs, then we will need to filter MOUSEMOTION only when button is depressed
        if pgEvent.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP]:
            x, y = pgEvent.pos
            return Events.MouseInputEvent(self.PyGameEventMappings[pgEvent.type], pygame.mouse.get_pressed(), x, y)

        return None


    def Notify(self, event):
        if isinstance(event, Events.TickEvent):
            for pgEvent in pygame.event.get():
                ev = self.ProcessPyGameEvent(pgEvent)
                if ev: super(InputController, self).Post(ev)
