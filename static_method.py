"""
A static method is bound to a class rather than the objects for that class
Unlike, class method, a static method cannot alter or change any variable value or state of the class.
Static methods do not have any knowledge related to the class.
For example, we want to add two numbers together, but we do not want our method to be used elsewhere, other than the class or through its instances,
so we will create a static method. It will not require any information related to class as it only requires the numbers it has to add,
but it will still fulfill its purpose as it is like a personal method that only the class has access to.
"""
class Employee:
    project = "Target"
    timings = "00:00 - 09:00"

    # @staticmethod
    # def str(string):
    #     print("This is Static Method" + string)

    @staticmethod       # Static decorator
    def str():      # we don't need to pass any 'self' or 'cls'
        print("This is Static Method")

# Employee.str(" Azram")
Employee.str()   # It can be accessed without any object, however, it can be accessed using any class or instance