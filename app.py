import logging
import OPi.GPIO as GPIO
import config
from time import sleep
from utils.logger import setup_logger
from api import HealthApi
from systems.temperature_regulation import TemperatureRegulationStateMachine, ErrorState
from utils.Sensors import TemperatureSensor
from queue import Queue

log = logging.getLogger(__name__)


def main():
    setup_logger({})
    log.info("Logger Initialized.")

    GPIO.setboard(GPIO.ZERO)
    GPIO.setmode(GPIO.BOARD)
    log.info("GPIO Initialized.")

    message_queue = Queue()
    log.info("Message Queue Initialized.")

    data = {"current_temp": 0.0,
            "desired_temp": config.stabilizer_desired_temp,
            "lower_limit": config.stabilizer_lower_temp_limit,
            "higher_limit": config.stabilizer_higher_temp_limit,
            "dangerous_temp": config.stabilizer_dangerous_temp,
            "pc_heat_level": 0.0,
            "error": False}

    temp_sensor = TemperatureSensor(0)
    log.info("Sensors Initialized.")

    state_machine = TemperatureRegulationStateMachine()
    log.info("State Machine Initialized.")
    thread = HealthApi(message_queue=message_queue)
    thread.start()
    log.info("API Initialized.")

    while not state_machine.in_state(ErrorState):
        data.update({"current_temp": temp_sensor.get()})
        message_queue.put(data)
        state_machine.update(data)
        sleep(3.)
    thread.join(10.0)


if __name__ == "__main__":
    main()
