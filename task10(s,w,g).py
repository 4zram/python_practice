"""
*************Snake, Water, Gun - The Game*************
The game will be between machine and player where the program will import random choices of the 3 and out
of total 10 chances, who ever has the highest winning score will win the game.
"""
import random
l = ["Snake", "Water", "Gun"]
auto = random.choice(l)
i=10
ph = 0
pm = 0
draw = 0
def snake():
    global ph, pm, draw
    if auto == "Snake":
        draw += 1
    elif auto == "Water":
        ph += 1
    elif auto == "Gun":
        pm += 1
    return 0
def water():
    global ph, pm, draw
    if auto == "Snake":
        pm += 1
    elif auto == "Water":
        draw += 1
    elif auto == "Gun":
        ph += 1
    return 0
def gun():
    global ph, pm, draw
    if auto == "Snake":
        ph += 1
    elif auto == "Water":
        pm += 1
    elif auto == "Gun":
        draw += 1
    return 0

while i>=0:
    take = input("S, W or G, Which one did you chose?\n")
    if take == "S":
        snake()
    elif take == "W":
        water()
    elif take == "G":
        gun()
    print(f"You have {i} chances!")
    i -= 1
if ph>pm:
    print("Congratulations! You won.\n")
else:
    print("\nBetter luck next time\n")
print(f"*****Game states:*****\n Computer won- {pm}\n You won - {ph}\n Draw - {draw}")