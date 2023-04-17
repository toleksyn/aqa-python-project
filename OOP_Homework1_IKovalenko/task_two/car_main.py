from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, model, make_year, engine_type):
        self.model = model
        self.make_year = make_year
        self.engine_type = engine_type

    @abstractmethod
    def drive(self):
        pass

    def print_car_info(self):
        print(f"Model: {self.model}\nMake Year: {self.make_year}")