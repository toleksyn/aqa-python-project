
from car import Car
from electric_car import ElectricCar
from ice_car import ICECar

electric_car = ElectricCar("Tesla Model S", 2022)
electric_car.print_car_info()
electric_car.drive()

ice_car = ICECar("Subaru", 2023)
ice_car.print_car_info()
ice_car.drive()