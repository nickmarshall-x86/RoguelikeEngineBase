import datetime

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
            self.Configs.Constants.DEBUG_INFO_KEY_CONTROLLER_NAME: self.ControllerName,
            self.Configs.Constants.DEBUG_INFO_KEY_EVENT_TIME: datetime.datetime.now()
        }

        self.Mediator.Post(event)