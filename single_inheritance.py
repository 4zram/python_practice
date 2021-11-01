"""
Class within a class is called inheritance. In this example, the 'Programmer' class is the child for the 'Employee' class.
Programmer class has the access to all the resources of the parent class and has it's own modifications or additional resources.
In the example here, parent class was Employee which contains the details of all the employees and child was Programmer class which
contains additional details for all the programmer amongst the employees.
"""
class Employee:
    project = "Target"
    leaves = 9
    timings = "00:00 - 09:00"

    # constructor
    def __init__(self, name, salary, exp):
        self.name = name
        self.salary = salary
        self.experience = exp

    # Function to print the output
    def prints(self):
        # print(f"Employee {self.name} receives {self.salary} salary and has {self.experience} years of experience.")
        return f"Employee {self.name} receives {self.salary} salary and has {self.experience} years of experience."

    # Method to change class variables
    @classmethod
    def changes(cls):
        cls.project = p
        cls.leaves = l
        cls.timings = t

    # Class stitched plain Method
    def plain(str):
        print("This is " + str)

    # Method to parse object attributes
    @classmethod
    def cut(cls, string):
        return cls(*string.split())

# Child class of the Employee class
class Programmer(Employee):
    wfh_leave = 7
    bonus_hours = "40/hour"

    # Construtor
    def __init__(self, name, salary, exp, lang):
        self.name = name
        self.salary = salary
        self.experience = exp
        self.language = lang

    # Function to print the output
    def printing(self):
        # print(f"Employee {self.name} receives {self.salary} salary and has {self.experience} years of experience.")
        return f"Employee {self.name} receives {self.salary} salary and has {self.experience} years of experience with the knowledge of {self.language} languages."

# Printing employees
deepak = Employee.cut("Deepak 45000 4")
shourya = Employee("Shorya", 30000, 4)

# Printing programmers
azram = Programmer("Azram", 28000, 4, ["python", "Cpp", "C", "yml"])
faraz = Programmer.cut("Azram 20 0 ['python','Cpp']")

# Printing arguments that is detached from object.
Employee.plain("Azram")

# Printing employee outputs
print(Employee.prints(deepak))
print(Employee.prints(shourya))

# Printing programmer outputs
print(azram.printing())
print(faraz.printing())