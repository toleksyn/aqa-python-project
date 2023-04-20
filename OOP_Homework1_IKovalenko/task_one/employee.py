
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, sex, employee_id):
        self.name = name
        self.sex = sex
        self.employee_id = employee_id
        self.salary = None

    @abstractmethod
    def calculate_salary(self):
        pass

    def print_salary(self):
        print(f'Name: {self.name}\nID: {self.employee_id}\nSalary: {self.salary}')