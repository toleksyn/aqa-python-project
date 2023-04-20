
from employee import Employee
from fixed_salary_employee import FixedSalaryEmployee
from hour_rate_employee import HourRateEmployee

fixed_employee = FixedSalaryEmployee("Igor Kovalenko", "M", "1234567")
fixed_employee.print_salary()

hour_employee = HourRateEmployee("Jane Lee", "F", "1111111", 20)
hour_employee.print_salary()