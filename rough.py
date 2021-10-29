print("Things to know before starting Game: \n", end="")
rules = {1: "You have to win against CPU\n",
         2: "Its like Stone, Paper, Scissor game\n  But instead of Stones, Papers and Scissors\n"
            "  Here is Snake, Water and Gun\n",
         3: "Snake drinks water and wins\n  Waters drowns the Gun and wins\n  Gun kills the Snake and wins\n",
         4: "The game will be played 10 times and you will then win or lose according to your score\n",
         5: "Type 's' for Snake, 'w' for Water, 'g' for Gun: \n"}
for key, value in rules.items():
    print(key, value, end="")