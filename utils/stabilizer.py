from utils.Actors import Heater, Cooler, EmptyBiSwitchActor
import logging
log = logging.getLogger(__name__)

class Stabilizer:
    def __init__(self):

        self.heater = Heater()
        self.cooler = EmptyBiSwitchActor()

    def update(self, environment):
        desired_temp = environment["desired_temp"]
        current_temp = environment["current_temp"]

        log.info("Current Temperature: {} C° ".format(current_temp))
        log.info("Desired Temperature: {} C° ".format(desired_temp))

        if current_temp <= desired_temp:
            log.info("Heating Up.")
            self.heat_up()
        else:
            log.info("Cooling Up.")
            self.cool_down()

    def cool_down(self):

        self.heater.off()
        self.cooler.on()

    def heat_up(self):
        self.cooler.off()
        self.heater.on()