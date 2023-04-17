
from car import Car

class ElectricCar(Car):
    def __init__(self, model, make_year):
        super().__init__(model, make_year, "electric")

    def drive(self):
        print("I`m driving on electricity")