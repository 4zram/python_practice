"""
Design a faulty calculator which will give the output of only the following wrong but the rest will be correct.
45*3 = 555, 56+9 = 77, 56/6 = 4
https://www.youtube.com/watch?v=VP8s9NiFToM&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=17
The program was not working earlier but I found out the issue. Instead of using symbols, I was taking
string inputs like ADD, SUB etc and for some reasons, that didn't work.
"""
var1 = int(input("What is your first number?\n"))
var2 = int(input("What is your second number?\n"))
var3 = input("With these numbers, you can do add(+), sub(-), mul(*), div(/). What do you want to do?\n")
# var3.upper()

if var3 == '+':
    if var1 == 56 and var2 == 9:
        print(
            f"{var1} + {var2} = 77")  # 'f' is called formatted string and is used to treat var as variables and not strings
    else:
        print(f"{var1} + {var2} = ", var1 + var2)
if var3 == '-':
    print(f"{var1} - {var2} = ", var1 - var2)
if var3 == '*':
    if var1 == 45 and var2 == 3:
        print(f"{var1} * {var2} = 555", )
    else:
        print(f"{var1} * {var2} = ", var1 * var2)
if var3 == '/':
    if var1 == 56 and var2 == 6:
        print(f"{var1} / {var2} = 4", )
    else:
        print(f"{var1} / {var2} = ", var1 / var2)
