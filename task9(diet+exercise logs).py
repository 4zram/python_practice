"""
Health management system!!!

You are a gym trainer and you have 3 clients Harry, Rohan, Hammad.
You have to create data of their diet and exercises and put them in separate files for each of them.
Use functions to access the users and their related data.
Provide the time stamp of the data logged and also provide readability of file option.

Use the following function for the time stamp -
def getdate():
    import datetime
    return datetime.datetime.now()
"""
def getdate():
    import datetime
    return datetime.datetime.now()

def harry_d():
    with open("harry_diet.txt", "a") as har:
        diet1 = "var"
        while diet1 != " ":
            diet1 = input("Enter the diet. Hit space if you want to exit\n")
            t = str(getdate())
            har.write("["+t+"]: "+diet1+"\n")
def rohan_d():
    with open("rohan_diet.txt", "a") as roh:
        diet2 = "var"
        while diet2 != " ":
            diet2 = input("Enter the diet. Hit space if you want to exit\n")
            t = str(getdate())
            roh.write("["+t+"]: "+diet2+"\n")
def hammad_d():
    with open("hammad_diet.txt", "a") as ham:
        diet3 = "var"
        while diet3 != " ":
            diet3 = input("Enter the diet. Hit space if you want to exit\n")
            t = str(getdate())
            ham.write("["+t+"]: "+diet3+"\n")
def harry_e():
    with open("harry_exercise.txt", "a") as har:
        diet1 = "var"
        while diet1 != " ":
            diet1 = input("Enter the diet. Hit space if you want to exit\n")
            t = str(getdate())
            har.write("["+t+"]: "+diet1+"\n")
def rohan_e():
    with open("rohan_exercise.txt", "a") as roh:
        diet2 = "var"
        while diet2 != " ":
            diet2 = input("Enter the diet. Hit space if you want to exit\n")
            t = str(getdate())
            roh.write("["+t+"]: "+diet2+"\n")
def hammad_e():
    with open("hammad_exercise.txt", "a") as ham:
        diet3 = "var"
        while diet3 != " ":
            diet3 = input("Enter the diet. Hit space if you want to exit\n")
            t = str(getdate())
            ham.write("["+t+"]: "+diet3+"\n")

rw = input("Press 'r' to read and Press 'w' to write to a file!\n")
if rw == "r":
    who = input("Which file do you want to read? Harry diet, Rohan diet, Hammad diet,\t"
                "Harry exercise, Rohan exercise, Hammad exercise\n")
    if who  == "Harry diet":
        f = open("harry_diet.txt")
        print(f.read())
        f.close()
    elif who == "Rohan diet":
        f = open("rohan_diet.txt")
        print(f.read())
        f.close()
    elif who == "Hammad diet":
        f = open("hammad_diet.txt")
        print(f.read())
        f.close()
    elif who == "Harry exercise":
        f = open("harry_exercise.txt")
        print(f.read())
        f.close()
    elif who == "Rohan exercise":
        f = open("rohan_exercise.txt")
        print(f.read())
        f.close()
    elif who == "Hammad exercise":
        f = open("hammad_exercise.txt")
        print(f.read())
        f.close()
elif rw == "w":
    who = input("Which file do you want to write to? Harry diet, Rohan diet, Hammad diet,\t"
                "Harry exercise, Rohan exercise, Hammad exercise\n")
    if who == "Harry diet":
        harry_d()
    elif who == "Rohan diet":
        rohan_d()
    elif who == "Hammad diet":
        hammad_d()
    elif who == "Harry exercise":
        harry_e()
    elif who == "Rohan exercise":
        rohan_e()
    elif who == "Hammad exercise":
        hammad_e()