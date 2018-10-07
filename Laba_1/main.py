
from car import Car
from weather import Weather
from сompetition import Competition


def start(cars: list, competition: Competition, weather: Weather):
    for car in cars:
        time = 0
        speed = 0

        for distance in competition.get_distance_range():
            if time == 0:
                speed = 1
            else:
                wind_speed = weather.get_wind_speed
                speed = (time / car.get_time_to_max) * car.get_max_speed
                if speed > wind_speed:
                    speed -= (car.get_drag_coef * wind_speed)
            time += float(1) / speed

        print("Car <%s> result: %f" % (car.name, time))

cars = [
        Car('ferrary', 340, 0.324, 26),
        Car('bugatti', 407, 0.39, 32),
        Car('toyota', 180, 0.25, 40),
        Car('lada', 180, 0.32, 56),
        Car('sx4', 180, 0.33, 44)
    ]

start(cars, Competition(10000), Weather(20))