from multiprocessing import Manager
from time import sleep

from systems.Heater import HeaterStateMachine, ErrorState
from utils.Sensors import Temperatur


def main():
    manager = Manager()
    data = manager.dict({"current_temp": 0.0,
                         "desired_temp": 25.0,
                         "max_temp": 30.0,
                         "pc_heat_level": 0.0,
                         "error": False})
    temp_sensor = Temperatur()
    state_machine = HeaterStateMachine();
    while not state_machine.in_state(ErrorState):
        data.update({"current_temp": temp_sensor.get()})
        state_machine.update(data)
        sleep(3.)


if __name__ == "__main__":
    main()