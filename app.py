from multiprocessing import Manager
from time import sleep

from api import HealthApi
from systems.Heater import HeaterStateMachine, ErrorState
from utils.Sensors import TemperatureSensor
from queue import Queue


def main():

    message_queue = Queue()
    data = {"current_temp": 0.0,
            "desired_temp": 25.0,
            "max_temp": 30.0,
            "pc_heat_level": 0.0,
            "error": False}

    temp_sensor = TemperatureSensor()
    state_machine = HeaterStateMachine()

    thread = HealthApi(message_queue=message_queue)
    thread.start()

    while not state_machine.in_state(ErrorState):
        data.update({"current_temp": temp_sensor.get()})
        message_queue.put(data)
        state_machine.update(data)
        sleep(3.)
    thread.join(10.0)


if __name__ == "__main__":
    main()
