import json
from constants import Constants

class Configuration:
    def __init__(self, configurationPath):
        self.Configs = None
        self.Constants = Constants()
        with open(configurationPath) as f:
            self.Configs = json.load(f)

    @property
    def Version(self):
        return self.Configs[self.Constants.CFG_KEY_VERSION]

    @property
    def Logging(self):
        return LoggingConfiguration(self.Configs[self.Constants.CFG_KEY_LOGGING], self.Constants)


class LoggingConfiguration():
    def __init__(self, cfgRoot, constants):
        self.Configs = cfgRoot
        self.Constants = constants

    @property
    def DefaultLogType(self):
        return self.Configs[self.Constants.CFG_LOGGING_KEY_DEFAULT_TYPE]

    def GetLoggingTypeForEvent(self, eventName):
        if eventName in self.Configs[self.Constants.CFG_LOGGING_KEY_EVENT_RULES]:
            return self.Configs[self.Constants.CFG_LOGGING_KEY_EVENT_RULES][eventName]
        else: return self.Configs[self.Constants.CFG_LOGGING_KEY_DEFAULT_TYPE]

