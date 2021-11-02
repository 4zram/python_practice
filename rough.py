
class Student:
    tmarks = 100
    subjects = 5

    # Constructor
    def __init__(self, name, std):
        self.name = name
        self.std = std

    # Print method
    def prints(self):
        return f"{self.name} of class {self.std}"

    #Edit class variable methods
    def edits(self, new_tmarks, new_subjects):
        self.tmarks = new_tmarks
        self.subjects = new_subjects

    # Class stitched prints
    @classmethod
    def plain(cls):
        print("This is just a plain printing.")

    @classmethod
    def cuts(cls, string):
        return cls(*string.split())

class Topper(Student):
    avg = 90
    attendance = 97

    # Constructor
    def __init__(self, name, std, score):
        self.name = name
        self.std = std
        self.score = score

    # Printing Method
    def pri(self):
        return f"{self.name} of class {self.std} has scored {self.score} marks and made us all proud."

deepak = Student.cuts("Deepak 10")
azram = Topper.cuts("Azram 10 97")
print(Student.prints(deepak))
Student.plain()
print(Topper.avg)
print(Topper.pri(azram))