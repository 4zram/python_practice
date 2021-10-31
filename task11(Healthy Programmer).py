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
import schedule
from datetime import datetime
from pygame import mixer
mixer.init()

def water():
    """ To Log the time user consumed water and to keep playing mp3 unless user did not input yes. """
    mixer.music.load("water.mp3")
    mixer.music.play()

    query = input("Did you drink water? [y/n]\n")
    if query.lower() == 'y':
        with open("water log.txt", "a") as fil:
            fil.write("["+str(datetime.now())+"] :"+"You drank water\n")
        mixer.music.stop()
    else:
        while query.lower() == 'y':
            mixer.music.stop()
            break

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
schedule.every(10).seconds.do(water)

# Eye exercise after every 20 min = 1200.0 sec
schedule.every(30).seconds.do(eyes)

# Exercise after every 45 min = 2700.0 sec
schedule.every(60).seconds.do(exercise)

if __name__ == '__main__':
    while True:
        a = 9
        # print("in while loop\n")
        for a in range(9,18):
            print(f"in for loop {a}\n")
            i = datetime.today()
            j = i.replace(second=a)
            print(i, "\n", j)
            time.sleep(2)
            if i == j:
                print("It is Time\n")
                schedule.run_pending()
                time.sleep(1)
            else:
                schedule.cancel_job(water)
                schedule.cancel_job(eyes)
                schedule.cancel_job(exercise)
        a += 1