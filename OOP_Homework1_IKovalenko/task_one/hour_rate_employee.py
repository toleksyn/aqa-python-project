
from employee import Employee

class HourRateEmployee(Employee):
    def __init__(self, name, sex, employee_id, hourly_rate):
        super().__init__(name, sex, employee_id)
        self.hourly_rate = hourly_rate
        self.salary = self.calculate_salary()

    def calculate_salary(self):
        return 20.8 * 8 * self.hourly_rate