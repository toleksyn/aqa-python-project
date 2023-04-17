
from student import Student

class PartTimeStudent(Student):
    def __init__(self, name, last_name, age, address):
        super().__init__(name, last_name, age, address)

    def study_type(self):
        return "I`m studying part time"