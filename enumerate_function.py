"""
enumerate function will retain every next value
"""

l = ["Oats", "Rajma", "Paw-Bhaji", "Lasagne", "Pasta", "Speghetti", "Pancakes", "Fried Rice"]

# Doing without enumerate method
i=0
for item in l:
    if i%2 == 0:
        print("Done without enumeration", item)
    i += 1

# Doing with enumerate method
for index, item in enumerate(l):
    if index%2 == 0:
        print("Doing with enumeration", item)