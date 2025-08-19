import time
import pygame
from plyer import notification
import schedule

pygame.mixer.init()

def alarm(song):
    print("🚨 Alarm function is running!")
    notification.notify(
        title="💧 Drink Water Reminder",
        message="It's time to drink water! Stay hydrated.",
        timeout=10  
    )
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    time.sleep(10) 
    stop_alarm()

def stop_alarm():
    pygame.mixer.music.stop()

def set_alarm(duration, song):
    print(f"🔄 Recurring alarm set every {duration} seconds.")
    schedule.every(duration).seconds.do(alarm, song)


def main():
    try:
        while True:
            set = int(input("For how many hours do you want to set the alarm? (1-12): "))
            if set in range(1, 13):
                break
            print("Please enter a value between 1 and 12.")
        seconds = set*60*60
        songpath = "C:/Users/User/OneDrive/Documents/python/python full stack/oops/project/birds.mp3"
        set_alarm(seconds, songpath)
        print("Alarm is running. Press Ctrl+C to stop.")
        while True:
            print("⏳ Checking for scheduled tasks...")
            schedule.run_pending()
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping the alarm...")
        stop_alarm()
        schedule.clear()
        print("The alarm has been stopped.")

if __name__ == "__main__":
    main()