"""
Class method is used to change the class instance variable values through an object instance.
Here, 'cls' parameter is used to take in the changes.
"""
class Student:
    total_marks = 100
    attendance = 200

    def __init__(self, n, m, a):
        self.name = n
        self.marks = m      #These are instance variable
        self.attendance = a

    def call(self):
        print(f"Student {self.name} has scored {self.marks} and has maintained {self.attendance}"
              f"attendance through this year")

    @classmethod        # class decorator
    def changes(cls, new_total_marks, new_total_attendance):
        cls.total_marks = new_total_marks
        cls.attendance = new_total_attendance

harry = Student("Harry", 75, "84%\t")
harry.changes(150, 100)
Student.call(harry)
print("Student total marks =", Student.total_marks, "\nStudent total attendance =", Student.attendance)