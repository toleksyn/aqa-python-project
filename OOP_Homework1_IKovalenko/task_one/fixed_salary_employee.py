
from employee import Employee


class FixedSalaryEmployee(Employee):
    def __init__(self, name, sex, employee_id):
        super().__init__(name, sex, employee_id)
        self.salary = 10000

    def calculate_salary(self):
        pass