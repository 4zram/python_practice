import time
from pygame import mixer
mixer.init()

# schedule.every(3).seconds.do(water)

if __name__ == '__main__':
    while True:
        # x = datetime.today()
        # schedule.run_pending()
        state = input("play(p)/pause(s)/exit(e)?")
        time.sleep(1)
        if state.lower() == 'p':
            print("Loading test.mp3")
            mixer.music.load("test.mp3")
            mixer.music.play()
        elif state.lower() == 's':
            print("Music stopped!")
            mixer.music.stop()
        else:
            break