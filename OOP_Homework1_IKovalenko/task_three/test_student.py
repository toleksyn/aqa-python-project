
from student import Student
from full_time_student import FullTimeStudent
from part_time_student import PartTimeStudent
from remote_student import RemoteStudent

full_time_student = FullTimeStudent("Adam", "Smith", 18, "123 Golden St")
full_time_student.print_student_info()

part_time_student = PartTimeStudent("John", "Snow", 20, "13 Shevchenko Ave")
part_time_student.print_student_info()

remote_student = RemoteStudent("Irena", "Adler", 22, "250 Baker St")
remote_student.print_student_info()