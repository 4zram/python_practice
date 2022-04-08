"""
***************Healthy Programmer***************
Water - Plays water.mp3 - 3.5L per shift consumption - drank
Eyes - plays eyes.mp3 - every 20 min - ey_done
Exercise - plays exercise.mp3 - 45 min - ex_done
We have to make a program to remind the programmer to do the above things in the described times/quantity.
The music should continue to play until he hit done.
To play music, we would need to use pygame module.
"""
import time
import schedule # For scheduling time intervals
from datetime import datetime   # For dealing with current time
from pygame import mixer    # For dealing with music
mixer.init()

# Water intake
def water():
    """ To Log the time user consumed water and to keep playing mp3 unless user did not input yes. """
    mixer.music.load("water.mp3")
    mixer.music.play()

    query = input("Did you drink water? [y/n]\n")
    if query.lower() == 'y':
        # Creating a log for water consumption time
        with open("water log.txt", "a") as fil:
            fil.write("["+str(datetime.now())+"] :"+"You drank water\n")
        mixer.music.stop()
    else:
        while query.lower() == 'y':
            mixer.music.stop()
            break

# Eyes exercise
def eyes():
    """ To play music unless user did not input yes """
    mixer.music.load("eyes.mp3")
    mixer.music.play()

    query = input("Did you do eye exercise? [y/n]\n")
    if query.lower() == 'y':
        mixer.music.stop()
    else:
        while query.lower() == 'y':
            mixer.music.stop()
            break

# Physical exercise
def exercise():
    """ To play music unless user did not input yes """
    mixer.music.load("exercise.mp3")
    mixer.music.play()

    query = input("Did you do exercise? [y/n]\n")
    if query.lower() == 'y':
        mixer.music.stop()
    else:
        while query.lower() == 'y':
            mixer.music.stop()
            break

# Water consumption after every 30 min = 1800.0 sec
schedule.every(1).minutes.do(water)
# print("hello")
# time.sleep(20)

# Eye exercise after every 20 min = 1200.0 sec
schedule.every(2).minutes.do(eyes)
# time.sleep(40)

# Exercise after every 45 min = 2700.0 sec
schedule.every(3).minutes.do(exercise)
# time.sleep(80)

if __name__ == '__main__':
    while True:
        a = 9
        # print("in while loop\n")
        for a in range(9,18):
            print(f"in for loop {a}\n")
            i = datetime.today()
            j = i.replace(minute=a)
            print(i, "\n", j)
            time.sleep(2)
            while i == j:
                print(f"It is Time {i}\n")
                schedule.run_pending()
                time.sleep(1)
        a += 1