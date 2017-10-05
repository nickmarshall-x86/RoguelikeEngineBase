from controllerBase import ControllerBase
from logController import LogController
import Events

class StateController(ControllerBase):
    def __init__(self, mediator, configuration):
        super(StateController, self).__init__("StateController", mediator, configuration)
        self.CurrentState = self.Configs.Constants.STATE_STARTUP
        self.Controllers = {}

    def SetUpInitialControllers(self):
        self.Controllers[self.Configs.Constants.CONTROLLER_LOGGING] = LogController(self.Mediator, self.Configs)

    def OnTick(self):
        if self.CurrentState == self.Configs.Constants.STATE_STARTUP:
            self.SetUpInitialControllers()

    def Notify(self, event):
        if isinstance(event, Events.TickEvent):
            self.OnTick()