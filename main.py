import sys
import os
import traceback
import Controllers
from Events import EventMediator
from configuration import Configuration

def LoadConfiguration():
    if len(sys.argv) > 1:
        return Configuration(sys.argv[1])
    return Configuration(os.path.join(os.getcwd(), "Data", "defaultConfigurations.json"))

if __name__ == '__main__':
    configuration = LoadConfiguration()
    
    mediator = EventMediator()

    clockController = Controllers.ClockController(mediator, configuration)
    stateController = Controllers.StateController(mediator, configuration)

    try:
        clockController.Run()
    except Exception as ex:
        print traceback.format_exc()
        print repr(ex)
        sys.exit(1)