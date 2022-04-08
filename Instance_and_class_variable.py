"""
OOP allows the variables to be used at the class level or the instance level.
Making use of class and instance variables can ensure that our code adheres to the DRY (don't repeat yourself) principle
to reduce repetition within code.
"""
class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print("Rohan's old leave", rohan.no_of_leaves)
print(rohan.__dict__)
# .__dict__ ; This maps the attribute name to its value. This is a dictionary that stores the name-value of an instance.
rohan.no_of_leaves = 9
#An instance can never change the class variable. Here, new attribute has been created for rohan but the class variable remains the same.
print(rohan.__dict__)
print("Rohan's new leave", rohan.no_of_leaves)
print("Harry's leave", harry.no_of_leaves)
print("Employee's leave", Employee.no_of_leaves)

# print(Employee.no_of_leaves)
# print(Employee.__dict__)
# Employee.no_of_leaves = 9
# print(Employee.__dict__)
# print(Employee.no_of_leaves)

