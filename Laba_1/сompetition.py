from Laba_1.weather import Weather

class Competition:
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, distance: int):
        self.distance = distance
        self._cars = set()

    def get_distance_range(self):
        return range(self.distance)

    def attach(self, observer):
        self._cars.add(observer)

    def notify(self):
        for car in self._cars:
            car.start(self.get_distance_range(), Weather(20))