from controllerBase import ControllerBase
from logController import LogController
from inputController import InputController
from viewInitializationController import ViewInitializationController

import constants as C
import Events

class StateController(ControllerBase):
    def __init__(self, mediator, configuration):
        super(StateController, self).__init__("StateController", mediator, configuration)
        self.CurrentState = C.STATE_STARTUP
        self.Controllers = {}

    def SetUpInitialControllers(self):
        self.Controllers[C.CONTROLLER_LOGGING] = LogController(self.Mediator, self.Configs)
        self.Controllers[C.CONTROLLER_INPUT] = InputController(self.Mediator, self.Configs)
        self.Controllers[C.CONTROLLER_VIEW_INIT] = ViewInitializationController(self.Mediator, self.Configs)

    def OnTick(self):
        if self.CurrentState == C.STATE_STARTUP:
            self.SetUpInitialControllers()

    def Notify(self, event):
        if isinstance(event, Events.TickEvent):
            self.OnTick()