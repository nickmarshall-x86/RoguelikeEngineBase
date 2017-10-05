from eventBase import EventBase

class QuitEvent(EventBase):
    def __init__(self):
        super(QuitEvent, self).__init__("QuitEvent")