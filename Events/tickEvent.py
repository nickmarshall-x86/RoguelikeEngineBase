from eventBase import EventBase

class TickEvent(EventBase):
    def __init__(self):
        super(TickEvent, self).__init__("TickEvent")