from utils.stabilizer import Stabilizer
from utils.state_machines import StateMachine, State
import logging

log = logging.getLogger(__name__)

class ErrorState(State):
    __state_name = "Error"

    def on_start(self):
        log.error("Emergency: Cooling Down!")
        Stabilizer().cool_down()

    def update(self, environment):
        environment["error"] = True

    def on_exit(self):
        pass


class NormalState(State):
    __state_name = "Normal"

    def __init__(self):
        self.stabilizer = Stabilizer()

    def on_start(self):
        pass

    def update(self, environment):
        self.stabilizer.update(environment)

    def on_exit(self):
        pass


class TemperatureRegulationStateMachine(StateMachine):
    def __init__(self):
        self.current_state = NormalState()

    def update(self, environment):
        if self.in_state(NormalState):
            if environment["current_temp"] >= environment["dangerous_temp"]:
                self._change_state(ErrorState)
        self.current_state.update(environment)

