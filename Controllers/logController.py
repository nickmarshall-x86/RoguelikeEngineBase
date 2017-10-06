from controllerBase import ControllerBase
import constants as C
import datetime
import os
import Events

class LogController(ControllerBase):
    def __init__(self, mediator, configuration):
        super(LogController, self).__init__("LogController", mediator, configuration)
        self.LogBuffer = []
        self.Timestamp = None

    def GenerateLogMessageForEvent(self, event):
        return "Event: {0} broadcast from {1} at {2}{3}".format(event.EventName, 
                event.DebugInformation[C.DEBUG_INFO_KEY_CONTROLLER_NAME],
                event.DebugInformation[C.DEBUG_INFO_KEY_EVENT_TIME],
                event.GetLoggingInformation())

    def LogToConsole(self, event):
        print self.GenerateLogMessageForEvent(event)

    def LogToFile(self, event):
        self.LogBuffer.append(self.GenerateLogMessageForEvent(event))
        if len(self.LogBuffer) > self.Configs.Logging.BufferSize:
            self.FlushLogToFile()

    def FlushLogToFile(self):
        if not self.Timestamp:
            self.Timestamp = str(datetime.datetime.now()).replace(' ','_').replace('.','').replace(":","-")
        with open(os.path.join(os.getcwd(), 'Logs', "Log_{0}.txt".format(self.Timestamp)), 'a') as f:
            while len(self.LogBuffer) > 0:
                f.write(self.LogBuffer.pop(0) + '\n')

    def Notify(self, event):
        loggingType = self.Configs.Logging.GetLoggingTypeForEvent(event.EventName)
        if loggingType == C.CFG_LOGGING_DEFAULTLOGTYPE_CONSOLE:
            self.LogToConsole(event)
        elif loggingType == C.CFG_LOGGING_DEFAULTLOGTYPE_FILE:
            self.LogToFile(event)

        if isinstance(event, Events.QuitEvent):
            self.FlushLogToFile()
