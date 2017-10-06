from controllerBase import ControllerBase
import Events
import pygame

class ViewInitializationController(ControllerBase):
    def __init__(self, mediator, configuration):
        super(ViewInitializationController, self).__init__("ViewInitializationController", mediator, configuration)
        self.IsViewInitialized = False
        self.Window = None
        pygame.init()

    def Notify(self, event):
        if isinstance(event, Events.TickEvent) and self.IsViewInitialized == False:
            self.Window = pygame.display.set_mode(self.Configs.Video.WindowSize)
            self.IsViewInitialized = True
            super(ViewInitializationController, self).Post(Events.ViewInitializedEvent(self.Window))