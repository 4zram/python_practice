"""
Public Access Modifier: Any one can access this class. All classes we have made so far were public by default.
Protected Access Modifier: The class itself and the inherited classes has access to them. This is recognised by single underscore (_)
Private Access Modifier: Only the class itself has the access to these resources and no one else can access them. This is recognised by 2 underscore (__)
Python does name mangling.
which means that every member with a double underscore will be changed to _object._class__variable when trying to call using an object.
The purpose of this is to warn a user so he does not use any private class variable or function by mistake without realizing its states.
"""

class Electronic_device:
    battery = "None"        # Public attribute
    power = "120W"

    # Constructor
    def __init__(self, name, usage, size):
        self.name = name
        self.usage = usage
        self.size = size

    # Method - Printing output
    def prints(self):
        return f"The device {self.name} is used for {self.usage} and is {self.size} in size."

    # Method - Parsing the string
    @classmethod
    def pars(cls, string):
        return cls(*string.split())

    # Class binded text
    @classmethod
    def plain(cls):
        return "This is an early electronic device!"


class Pocket_gadget(Electronic_device):
    _battery = "500mAH"     # Protected attribute
    _charger = "10W"
    _power = "60W"

    # Method - Class binded text printing
    @classmethod
    def print(cls):
        return "This is a primitive version of Hand-Held Electronic Device"


class Phone(Pocket_gadget):
    __battery = "3000mAH"       # Private attribute
    __charger = "30W"
    __power = "20W"

    # Method - Class binded text printing
    @classmethod
    def pri(cls):
        return "This is an advanced version of the Electronic Device."

computer = Electronic_device.pars("Computer Computing 12x12")
laptop = Electronic_device.pars("Laptop Multiple-Powerful-Things 15inch")
tablet = Electronic_device.pars("Tablet Multiple-Things 10inch")

print("Electronic_device: ", Electronic_device.battery, "Battery",Electronic_device.power, "Power")
print("Pocket_gadget: ", Pocket_gadget._battery, "Battery", Pocket_gadget._power, "Power",Pocket_gadget._charger,"Charger")
print("Phone: ", Phone._Phone__battery, "Battery", Phone._Phone__power, "Power", Phone._Phone__charger, "Charger")
# We would need to call the private attribute using the _Phone here

print(Electronic_device.prints(computer))
print(Pocket_gadget.prints(laptop))
print(Phone.prints(tablet))