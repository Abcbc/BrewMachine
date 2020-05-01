class StateMachine:
    """
    
    """
    def __init(self):
        self.current_state = None

    def update(self, environment):
        """
        This updates the State Machine.
        :param environment: this is the observable environment of the State Machine.The state Machine reacts to it.
        """
        pass

    def _change_state(self, stateClass):
        self.current_state.on_exit()
        self.current_state = stateClass()
        self.current_state.on_start()

    def _is_state(self, state):
        return isinstance(self.current_state, state)


class State:
    """
    State interface.
    """
    def __init__(self):
        pass

    def on_start(self):
        pass

    def update(self, environment):
        pass

    def on_exit(self):
        pass


