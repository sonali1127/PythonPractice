import time
import schedule
def alarm():
    print("Time's up! This is a recurring alarm.")
# Schedule the alarm to run every 5 seconds
job=schedule.every(5).seconds.do(alarm)
# Keep the script running
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping the alarm...")
    schedule.cancel_job(job)  # Cancel the specific job
    print("The alarm has been stopped.")