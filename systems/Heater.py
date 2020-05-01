from utils.state_machines import StateMachine, State


class ErrorState(State):
    __state_name = "Error"

    def on_start(self):
        print("Going to sleep.")

    def update(self, environment):
        print("Sleeping.")

    def on_exit(self):
        print("Waking up.")


class NormalState(State):
    __state_name = "Normal"

    def __init__(self):
        self.stabilizer = Stabilizer()

    def on_start(self):
        print("Going to sleep.")

    def update(self, environment):
        self.stabilizer.update(environment)

    def on_exit(self):
        print("Waking up.")


class HeaterStateMachine(StateMachine):
    def __init__(self):
        self.current_state = NormalState()

    def update(self, environment):
        if self._is_state(NormalState):
            if environment["current_temperature"] >= environment["panic_temperature"]:
                self._change_state(ErrorState)
        self.current_state.update(environment)
