import schedule
import time

def check_updates_periodically():
    notifier.check_for_updates()

schedule.every(1).hour.do(check_updates_periodically)

while True:
    schedule.run_pending()
    time.sleep(1)
