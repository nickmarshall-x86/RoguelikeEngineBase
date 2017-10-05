class EventBase(object):
    def __init__(self, eventName):
        self.EventName = eventName
        self.DebugInformation = None

    def GetLoggingInformation(self):
        return ""