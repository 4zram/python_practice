"""
Constructors assign values to the variables and data-members of the class upon object creation.
They are defined within the class.
Constructors are of two types:
1. Default (which is shown here)
    def __init__(self):
        # body of the constructor
2. Parameterised (which is declared with parameters as shown in the running code below)
Method has 'self' parameter which maps to the instances of the current class
"""
class Employee:
    print("In the class")
    no_of_leaves = 8    #This is an attribute of Employee class
    # This is a parameterised constructor
    def __init__(self, aname, asalary, arole):
        print("In the constructor")
        self.name = aname
        self.salary = asalary       # These are instance variable.
        self.role = arole

    # This is called a method which aims to reflect the object details.
    def printdetails(self):
        print(f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}")
       # return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 255, "Instructor")

# rohan = Employee()
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

# print(harry)    # Is an Employee object mapped to a location.
# print(harry.salary)
Employee.printdetails(harry)    #return won't work for this, hence was commented out.
print(Employee.printdetails(harry))