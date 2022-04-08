# Create a list and print only numbers of the list and that should be greater than 6

l = [3, 5,6,"this","that",78,"harmony",23,"disdain"]
for item in l:
    if str(item).isnumeric() and item>6:    #typecasting item in string and then checking for numerics
        print(item)