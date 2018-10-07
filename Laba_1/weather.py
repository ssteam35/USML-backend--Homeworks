from random import randint


class Weather:
    def __init__(self, wind_speed):
        self.wind_speed = wind_speed

    @property
    def get_wind_speed(self):
        return randint(0, self.wind_speed)