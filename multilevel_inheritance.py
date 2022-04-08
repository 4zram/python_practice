"""
Multilevel Inheritance has 3 class level - BASE, INTERMEDIATE, DERIVED
Here, Phone has inherited from Pocket_gadget which has inheritance from Electronic_device.
Hence, the print statement which lies in the GrandParent class works for all since it's resouces are shared across them all.
"""

class Electronic_device:
    battery = "None"
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
    battery = "500mAH"
    charger = "10W"
    power = "60W"

    # Method - Class binded text printing
    @classmethod
    def print(cls):
        return "This is a primitive version of Hand-Held Electronic Device"


class Phone(Pocket_gadget):
    battery = "3000mAH"
    charger = "30W"
    power = "20W"

    # Method - Class binded text printing
    @classmethod
    def pri(cls):
        return "This is an advanced version of the Electronic Device."

computer = Electronic_device.pars("Computer Computing 12x12")
laptop = Electronic_device.pars("Laptop Multiple-Powerful-Things 15inch")
tablet = Electronic_device.pars("Tablet Multiple-Things 10inch")

print("Electronic_device: ", Electronic_device.battery, "Battery",Electronic_device.power, "Power")
print("Pocket_gadget: ", Pocket_gadget.battery, "Battery", Pocket_gadget.power, "Power",Pocket_gadget.charger,"Charger")
print("Phone: ", Phone.battery, "Battery", Phone.power, "Power", Phone.charger, "Charger")

print(Electronic_device.prints(computer))
print(Pocket_gadget.prints(laptop))
print(Phone.prints(tablet))