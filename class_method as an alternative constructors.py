
class Student:
    total_marks = 100
    attendance = "200 days"

    def __init__(self, name, marks, attendance):
        self.name = name
        self.marks = marks
        self.attendance = attendance

    def call(self):
        print(f"Student {self.name} has scored {self.marks} marks and was {self.attendance} attendent")

    @classmethod
    def parse(cls, new_total_marks, new_attendance):
        cls.total_marks = new_total_marks
        cls.attendance = new_attendance

# Class method as a alternative constructor
    @classmethod
    def str(cls, string):
        # p = string.split("-")     # Parse and creates a list of the things. The splitting action can happen over "-" if "-" was there instead of whitespace
        # print(p)
        # return cls(p[0], p[1], p[2])
        return cls(*string.split())      # Args and Kwargs concept used here!

# harry = Student("Harry", 83, "92%")
harry = Student.str("Harry 82 95%")     # The splitting action happened over the white spaces.
rohan = Student.str("Rohan 74 86%")
karan = Student("Karan", 95, "72%")

Student.call(harry)
Student.call(rohan)
Student.call(karan)

# print(harry)      # Will show address of harry
# print(karan.total_marks)