from controllerBase import ControllerBase
from logController import LogController
from inputController import InputController
from viewInitializationController import ViewInitializationController
from dungeonCommandController import DungeonCommandController
from dungeonViewController import DungeonViewController

import constants as C
import Events

class StateController(ControllerBase):
    def __init__(self, mediator, configuration):
        super(StateController, self).__init__("StateController", mediator, configuration)
        self.CurrentState = C.STATE_STARTUP
        self.Controllers = {}

    def UnregisterController(self, controllerKey):
        self.Mediator.UnregisterListener(self.Controllers[controllerKey])
        del self.Controllers[controllerKey]
        super(StateController, self).Post(Events.LogEvent("INFO", "Unregistered Controller: {0}".format(controllerKey)))

    def RegisterController(self, controllerKey, controller):
        self.Controllers[controllerKey] = controller(self.Mediator, self.Configs)
        super(StateController, self).Post(Events.LogEvent("INFO", "Registered Controller: {0}".format(controllerKey)))

    def SetState(self, state):
        self.CurrentState = state
        super(StateController, self).Post(Events.LogEvent("INFO", "Changing State to: {0}".format(state)))

    def SetUpInitialControllers(self):
        self.RegisterController(C.CONTROLLER_LOGGING, LogController)
        self.RegisterController(C.CONTROLLER_INPUT, InputController)
        self.RegisterController(C.CONTROLLER_VIEW_INIT, ViewInitializationController)

        self.SetState(C.STATE_INITIALIZING)

    def OnTick(self):
        if self.CurrentState == C.STATE_STARTUP:
            self.SetUpInitialControllers()

    def OnViewInitialized(self, event):
        self.UnregisterController(C.CONTROLLER_VIEW_INIT)
        self.RegisterController(C.CONTROLLER_DUNGEON_COMMAND, DungeonCommandController)
        self.RegisterController(C.CONTROLLER_VIEW_DUNGEON, DungeonViewController)
        self.Controllers[C.CONTROLLER_VIEW_DUNGEON].SetWindow(event.Window)
        
    def Notify(self, event):
        if isinstance(event, Events.TickEvent):
            self.OnTick()
        if isinstance(event, Events.ViewInitializedEvent):
            self.OnViewInitialized(event)