
from abc import ABC, abstractmethod

class Student(ABC):
    def __init__(self, name, last_name, age, address):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.address = address

    @abstractmethod
    def study_type(self):
        pass

    def print_student_info(self):
        print(f"Name: {self.name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Study type: {self.study_type()}")