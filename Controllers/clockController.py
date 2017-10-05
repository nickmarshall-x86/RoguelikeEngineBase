from controllerBase import ControllerBase
import Events

class ClockController(ControllerBase):
    def __init__(self, mediator, configuration):
        super(ClockController, self).__init__("ClockController", mediator, configuration)
        self._IsRunning = True

    def Notify(self, event):
        if isinstance(event, Events.QuitEvent):
            self._IsRunning = False

    def Run(self):
        self._IsRunning = True
        while self._IsRunning:
            super(ClockController, self).Post(Events.TickEvent())
