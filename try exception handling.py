"""
If we provide a string to and int variable, the program will stop right there and throw some error.
If there is something important that was supposed to be executed which is present after the error line then,
those line of codes won't be executed. To eliminate this problem, we user try and exception.
"""
a = input("Your first number")
b = input("Your second number")

try:
    print("The sum is:", int(a)+int(b))
except Exception as e:
    print(e)

print("Some important line of codes which was supposed to be executed.")

# So by this way, the important line of codes will be executed even if there is a chance of code flow break