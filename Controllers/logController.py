from controllerBase import ControllerBase
import constants as C

class LogController(ControllerBase):
    def __init__(self, mediator, configuration):
        super(LogController, self).__init__("LogController", mediator, configuration)
        self.LogBuffer = []

    def GenerateLogMessageForEvent(self, event):
        return "Event: {0} broadcast at {1} from {2}{3}".format(event.EventName, 
                event.DebugInformation[C.DEBUG_INFO_KEY_CONTROLLER_NAME],
                event.DebugInformation[C.DEBUG_INFO_KEY_EVENT_TIME],
                event.GetLoggingInformation())

    def LogToConsole(self, event):
        print self.GenerateLogMessageForEvent(event)

    def Notify(self, event):
        if self.Configs.Logging.GetLoggingTypeForEvent(event.EventName) == C.CFG_LOGGING_DEFAULTLOGTYPE_CONSOLE:
            self.LogToConsole(event)
