class Employee:
    num_leaves = 8
    project = "Target"
    manager = "Satish Nadig"

print("Employee's common details", Employee.__dict__)

def __init__(self, x, y, z):
    self.name = x
    self.salary = y
    self.experience = z

harry = Employee("Rohan", 45000, "4 Years")
print(harry.salary)