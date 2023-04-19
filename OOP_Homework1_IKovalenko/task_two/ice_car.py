
from car import Car

class ICECar(Car):
    def __init__(self, model, make_year):
        super().__init__(model, make_year, "gas")

    def drive(self):
        print("I`m driving on gas")