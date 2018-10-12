import abc

class AbstractCars:
    @abc.abstractmethod
    def start(self, distance_range, weather):
        pass

class UpgradedCar(AbstractCars):
    def __init__(self, car):
        self._car = car

    def start(self, distance_range, weather):
        self._car.name = "Upgraded_" + self._car.name
        self._car.max_speed *= 1.5
        self._car.drag_coef += 0.5
        self._car.start(distance_range, weather)


class Car(AbstractCars):
    def __init__(self, name: str, max_speed, drag_coef, time_to_max):
        self.name = name
        self.time_to_max = time_to_max
        self.drag_coef = drag_coef
        self.max_speed = max_speed


    @property
    def get_name(self):
        return self.name

    @property
    def get_time_to_max(self):
        return self.time_to_max

    @property
    def get_drag_coef(self):
        return self.drag_coef

    @property
    def get_max_speed(self):
        return self.max_speed

    def start(self, distance_range, weather):
        time = 0
        for _ in distance_range:
            if time == 0:
                speed = 1
            else:
                wind_speed = weather.get_wind_speed
                speed = (time / self.get_time_to_max) * self.get_max_speed
                if speed > wind_speed:
                    speed -= (self.get_drag_coef * wind_speed)
            time += float(1) / speed

        print("Car <%s> result: %f" % (self.name, time))