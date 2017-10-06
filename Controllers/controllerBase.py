import datetime
import constants as C

class ControllerBase(object):
    def __init__(self, controllerName, mediator, configurations):
        self.ControllerName = controllerName
        self.Mediator = mediator
        self.Mediator.RegisterListener(self)
        self.Configs = configurations
        
    def Notify(self, event):
        pass

    def Post(self, event):
        event.DebugInformation = {
            C.DEBUG_INFO_KEY_CONTROLLER_NAME: self.ControllerName,
            C.DEBUG_INFO_KEY_EVENT_TIME: datetime.datetime.now()
        }

        self.Mediator.Post(event)