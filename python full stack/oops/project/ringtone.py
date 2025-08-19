import time
from playsound import playsound

def set_alarm_with_sound(seconds, sound_file):
    print(f"Alarm set for {seconds} seconds.")
    time.sleep(seconds)
    print("Time's up! Playing sound...")
    playsound(sound_file)  # Play the specified sound file

# Example: Set an alarm for 5 seconds and play a sound
set_alarm_with_sound(5, "C:/Users/User/OneDrive/Documents/python/python full stack/oops/project/birds.mp3")