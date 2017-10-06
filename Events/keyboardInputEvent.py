from eventBase import EventBase

class KeyboardInputEvent(EventBase):
    def __init__(self, keyboardEventType, keyboardKey):
        super(KeyboardInputEvent, self).__init__("KeyboardInputEvent")
        self.EventType = keyboardEventType
        self.Key = keyboardKey

    def GetLoggingInformation(self):
        return "\n Event Type: {0}, Key: {1}".format(self.EventType, self.Key)