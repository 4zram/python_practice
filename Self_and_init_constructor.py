"""
Constructors assign values to the variables and data-members of the class upon object creation
Constructors are of two types:
1. Default (which is shown here)
2. Parameterised (which is declared with parameters as shown in the running code below)
def __init__(self):
    # body of the constructor

Method has 'self' parameter which maps to the instances of the current class
"""
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    # This is called a method which aims to reflect the object details.
    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 255, "Instructor")

# rohan = Employee()
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

print(harry.salary)