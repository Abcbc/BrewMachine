import random as r
class Temperatur:

    def __init__(self):
        pass

    def get(self):
        return r.choice([20.0+x*0.2 for x in range(50)])