from eventBase import EventBase

class MouseInputEvent(EventBase):
    def __init__(self, mouseEventType, button, x, y):
        super(MouseInputEvent, self).__init__("MouseInputEvent")
        self.EventType = mouseEventType
        self.Button = button
        self.X = x
        self.Y = y

    def GetLoggingInformation(self):
        return "\n Event Type: {0}, Button: {1}, X: {2}, Y: {3}".format(self.EventType, self.Button, self.X, self.Y)