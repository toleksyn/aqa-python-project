
from student import Student

class FullTimeStudent(Student):
    def __init__(self, name, last_name, age, address):
        super().__init__(name, last_name, age, address)

    def study_type(self):
        return "I`m studying full time"