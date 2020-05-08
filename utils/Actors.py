import config
import OrangePi.GPIO as GPIO


class BiSwitchActor:
    def __init__(self, pin, on, off):
        self.PIN = pin
        self.ON = on
        self.OFF = off
        GPIO.setup(self.PIN, GPIO.OUT)

    def on(self):
        GPIO.output(self.PIN, self.ON)

    def off(self):
        GPIO.output(self.PIN, self.OFF)


class EmptyBiSwitchActor(BiSwitchActor):

    def __init__(self):
        pass

    def on(self):
        pass

    def off(self):
        pass


class Cooler(BiSwitchActor):
    """
    """
    def __init__(self):
        super().__init__(pin=config.actor_cooler_pin,
                         on=config.actor_cooler_on,
                         off=config.actor_cooler_off)


class Heater(BiSwitchActor):
    def __init__(self):
        super().__init__(pin=config.actor_heater_pin,
                         on=config.actor_heater_on,
                         off=config.actor_heater_off)

