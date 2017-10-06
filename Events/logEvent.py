from eventBase import EventBase

class LogEvent(EventBase):
    def __init__(self, level, message):
        super(LogEvent, self).__init__("LogEvent")
        self.Level = level
        self.Message = message

    def GetLoggingInformation(self):
        return "\n\t{0}: {1}".format(self.Level, self.Message)