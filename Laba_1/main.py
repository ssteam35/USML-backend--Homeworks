from Laba_1.car import Car, UpgradedCar
from Laba_1.сompetition import Competition

def main():
    competition = Competition(10000)
    cars = [
        Car('ferrary', 340, 0.324, 26),
        Car('bugatti', 407, 0.39, 32),
        UpgradedCar(Car('toyota', 180, 0.25, 40)),
        UpgradedCar(Car('lada', 180, 0.32, 56)),
        Car('sx4', 180, 0.33, 44)
    ]
    for car in cars:
        competition.attach(car)
    competition.notify()

main()

