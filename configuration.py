import json
import constants as C
class Configuration:
    def __init__(self, configurationPath):
        self.Configs = None
        with open(configurationPath) as f:
            self.Configs = json.load(f)

    @property
    def Version(self):
        return self.Configs[C.CFG_KEY_VERSION]

    @property
    def Logging(self):
        return LoggingConfiguration(self.Configs[C.CFG_KEY_LOGGING])

    @property
    def Video(self):
        return VideoConfiguration(self.Configs[C.CFG_KEY_VIDEO])


class LoggingConfiguration():
    def __init__(self, cfgRoot):
        self.Configs = cfgRoot

    @property
    def DefaultLogType(self):
        return self.Configs[C.CFG_LOGGING_KEY_DEFAULT_TYPE]

    @property
    def BufferSize(self):
        return self.Configs[C.CFG_LOGGING_KEY_BUFFERSIZE]

    def GetLoggingTypeForEvent(self, eventName):
        if eventName in self.Configs[C.CFG_LOGGING_KEY_EVENT_RULES]:
            return self.Configs[C.CFG_LOGGING_KEY_EVENT_RULES][eventName]
        else: return self.Configs[C.CFG_LOGGING_KEY_DEFAULT_TYPE]

class VideoConfiguration():
    def __init__(self, cfgRoot):
        self.Configs = cfgRoot

    @property
    def WindowSize(self):
        return (self.Configs[C.CFG_VIDEO_WINDOWX], self.Configs[C.CFG_VIDEO_WINDOWY])
    