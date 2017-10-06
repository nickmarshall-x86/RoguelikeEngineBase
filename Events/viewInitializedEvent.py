from eventBase import EventBase

class ViewInitializedEvent(EventBase):
    def __init__(self, window):
        super(ViewInitializedEvent, self).__init__("ViewInitializedEvent")
        self.Window = window