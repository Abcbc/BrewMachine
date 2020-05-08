import os


class TemperatureSensor:

    def __init__(self, number):
        self.ignore = ["w1_bus_master1"]
        self.path = "/sys/bus/w1/devices"
        self.sensors = [x for x in os.listdir(self.path) if x not in self.ignore]
        self.selected_number = number

    def get(self):
        result = -1.0
        sensor = self.sensors[self.selected_number]
        with open("/".join([self.path, sensor, "w1_slave"])) as f:
            for line in f:
                if "t=" in line:
                    result = float(line.split()[-1].replace("t=", "")) / 1000
        return result