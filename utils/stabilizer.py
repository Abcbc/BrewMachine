from utils.Actors import Heater, Cooler, EmptyBiSwitchActor
import logging
log = logging.getLogger(__name__)

class Stabilizer:
    def __init__(self):
        self.efficients = 1.0
        self.heater = Heater()
        self.cooler = EmptyBiSwitchActor()

    def update(self, environment):
        desired_temp = environment["desired_temp"]
        current_temp = environment["current_temp"]
        lower_limit = environment["lower_limit"]
        higher_limit = environment["lower_limit"]
        self.calculate_efficiency(current_temp, desired_temp)
        
        log.info("Current Temperature: {} C° ".format(current_temp))
        log.info("Desired Temperature: {} C° ".format(desired_temp))
        log.info("Efficiency: {}".format(self.efficients))

        if current_temp < lower_limit:
            log.info("Heating Up.")
            self.heat_up()
        elif current_temp >= higher_limit:
            log.info("Cooling Up.")
            self.cool_down()
        else:
            log.info("Stay in current mode.")

    def calculate_efficiency(self, current_temp, desired_temp):
        self.efficients /= 3
        self.efficients += 2 / 3 * (abs(desired_temp - current_temp) / desired_temp)
        self.efficients /= 2

    def cool_down(self):

        self.heater.off()
        self.cooler.on()

    def heat_up(self):
        self.cooler.off()
        self.heater.on()