from utils.Actors import Heater, Cooler, EmptyBiSwitchActor


class Stabilizer:
    def __init__(self):
        self.heater = Heater()
        self.cooler = EmptyBiSwitchActor()

    def update(self, environment):
        desired_temp = environment["desired_temp"]
        current_temp = environment["current_temp"]

        if current_temp <= desired_temp:
            self.heat_up()
        else:
            self.cool_down()

    def cool_down(self):
        self.heater.off()
        self.cooler.on()

    def heat_up(self):
        self.cooler.off()
        self.heater.on()