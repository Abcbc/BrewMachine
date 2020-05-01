from unittest import TestCase

from utils.state_machines import StateMachine, State


class WorkState(State):
    __state_name = "Work"

    def on_start(self):
        print("Going to work.")

    def update(self, environment):
        print("Working.")

    def on_exit(self):
        print("Leaving work.")


class HomeState(State):
    __state_name = "Home"

    def on_start(self):
        pass

    def update(self, environment):
        print("At Home.")

    def on_exit(self):
        pass


class BedState(State):
    __state_name = "Bed"

    def on_start(self):
        print("Going to sleep.")

    def update(self, environment):
        print("Sleeping.")

    def on_exit(self):
        print("Waking up.")


class WorkStateMachine(StateMachine):
    def __init__(self):
        self.current_state = HomeState()

    def update(self, environment):
        if self._is_state(HomeState):
            if environment == "SLEEP":
                self._change_state(BedState)
            elif environment == "TAKE_TRAIN":
                self._change_state(WorkState)
        elif self._is_state(BedState):
            if environment == "WAKE":
                self._change_state(HomeState)
        elif self._is_state(WorkState):
            if environment == "TAKE_TRAIN":
                self._change_state(HomeState)

        self.current_state.update(environment)


class TestStateMachine(TestCase):

    def test_update_simple_workday(self):
        state_machine = WorkStateMachine()
        print("Test1")
        state_machine.update("TAKE_TRAIN")
        state_machine.update("DO_NOTHING")
        state_machine.update("GET_A_COFFEE")
        state_machine.update("DO_A_LITTLE_BIT_OF_WORK")
        state_machine.update("TAKE_TRAIN")
        self.assertIsInstance(state_machine.current_state, HomeState)

    def test_update_simple_sleep_day(self):
        state_machine = WorkStateMachine()
        print("Test2")
        state_machine.update("SLEEP")
        state_machine.update("WAKE")
        self.assertIsInstance(state_machine.current_state, HomeState)

    def test_update_simple_sleep_at_work(self):
        state_machine = WorkStateMachine()
        print("Test3")
        state_machine.update("TAKE_TRAIN")
        state_machine.update("SLEEP")
        state_machine.update("SLEEP")
        self.assertIsInstance(state_machine.current_state, WorkState)