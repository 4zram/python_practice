"""
The Gussing Game!
The player will be given 10 guess and he has to guess the number as per the output.
His number of guess will be displayed and he will be declared winner or looser as per his number of guess
"""
a = 17
count = 0
while (True):
    b = int(input("Enter your guess number:\n"))
    count = count + 1
    left = 10 - count
    if left>0:
        if b>17:
            print("Your number is greater!\n",f"You have {left} guess left\n")
        elif b<17:
            print("Your number is smaller!\n",f"You have {left} guess left\n")
        elif b==17:
            print("Congrations! You won!\n",f"You took {count} guess\n")
            break
    if left==0:
        print("Sorry! You are out of guesses.")
        break