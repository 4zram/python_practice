"""
Multiple inheritance is done when one class is derived from multiple class. This is very similar to Single inheritance but here the child
inherits the features of both the parent class.
Order of parent class call in child method should be attended with great attention. Whichever is written first will be called for its resources first.
So if Employee is written first, the program will run according to the resources of the Employee class and then Player class.

Multi-Inheritance has 2 class level BASE AND DERIVED class levels.

Multiple inheritance causes diamond problems which most programming languages could not solve. Hence, it's recommended to avoid multiple inheritance.
"""
# Parent class 1
class Employee:
    leaves = 9
    project = "Target"
    timings = "00:00 - 09:00"

    # Constructor
    def __init__(self, name, salary, experience):
        self.name = name
        self.salary = salary
        self.experience = experience

    # Method - Edits to class variables
    def edits(self, l, p, t):
        self.leaves = l
        self.project = p
        self.timings = t

    # Method - Print output
    def prints(self):
        print(f"{self.name} gets {self.salary} salary and has {self.experience} experience.")

    # In-build class prints
    @classmethod
    def plain(cls):
        print("This is just a plain text built-in just to the class.")

    # Method - string parsing
    @classmethod
    def cut(cls, string):
        return cls(*string.split())

# Parent class 2
class Player:
    club = 4
    fund = 10,000

    # Constructor
    def __init__(self, name, salary, experience, game):     # When methods of same name are used then its called overriding.
        self.name = name
        self.salary = salary
        self.experience = experience
        self.game = game

    # Method - Printing
    def playerprint(self):
        print(f"{self.name} plays {self.game} games")

# Child class 2
class Programmer(Employee, Player):     # The order of parent class here should be taken in great consideration.
    leaves = 8
    wfh = 6

    # Constructor
    def __init__(self, name, salary, experience, game, language):
        self.name = name
        self.salary = salary
        self.experience = experience
        self.game = game
        self.language = language

    # Method - Printing
    def printsdo(self):
        print(f"{self.name} playes {self.game} and knows {self.language} languages.")

deepak = Programmer.cut("Deepak 97000 4 ['cricket','football'] ['python','cpp','verilog']")
Programmer.printsdo(deepak)