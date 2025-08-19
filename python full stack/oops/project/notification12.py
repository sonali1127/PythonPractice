import time
from plyer import notification
def set_alarm_with_notification(seconds, title, message):
    print(f"Alarm set for {seconds} seconds.")
    time.sleep(seconds)
    notification.notify(
        title=title,
        message=message,
        timeout=10  # Notification will disappear after 10 seconds
    )

# Example: Set an alarm for 5 seconds and show a desktop notification
set_alarm_with_notification(5, "Alarm", "Time's up!")