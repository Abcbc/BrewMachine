#import OrangePi.GPIO as GPIO
from utils.Actors import Heater, Cooler


class Stabilizer:
    def __init__(self):
        self.heater = Heater()
        self.cooler = Cooler()

        #self.COOLING_PIN = 12
        #self.HEATING_PIN = 11
        #self.ON = 0
        #self.OFF = 1
        #GPIO.setboard(GPIO.ZERO)
        #GPIO.setmode(GPIO.BOARD)
        #GPIO.setup(self.HEATING_PIN, GPIO.OUT)
        #GPIO.output(self.HEATING_PIN, self.OFF)
        #GPIO.setup(self.COOLING_PIN, GPIO.OUT)
        #GPIO.output(self.COOLING_PIN, GPIO.OFF)


    def update(self, environment):
        desired_temp = environment["desired_temp"]
        current_temp = environment["current_temp"]

        if current_temp <= desired_temp:
            self.heat_up()
        else:
            self.cool_down()

    def cool_down(self):
        print("Start cooldown.")
        self.heater.off()
        self.cooler.on()
        #GPIO.output(self.HEATING_PIN, self.OFF)
        #GPIO.output(self.COOLING_PIN, self.ON)

    def heat_up(self):
        #GPIO.output(self.COOLING_PIN, self.OFF)
        #GPIO.output(self.HEATING_PIN, self.ON)
        self.cooler.off()
        self.heater.on()