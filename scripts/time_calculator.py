# dependencies
import datetime
from datetime import timedelta

def add_time(start, duration, weekday = False):

    # reformatting 'start'; w/ help from GeeksforGeeks...
    if start.strip()[-2:] == "AM" and start.strip()[:2] == "12":
        new_start = "00" + start[2:-2]
    elif start.strip()[-2:] == "AM":
        new_start = start[:-2]
    elif start.strip()[-2:] == "PM" and start.strip()[:2] == "12":
        new_start = start[:-2]
    else:
        new_start = str(int(start.strip()[:2]) + 12) + start.strip()[2:5]

    # found from kite.com...
    start_time = datetime.time(hour=int(new_start[:2]), minute=int(new_start[-2:]))
    if len(duration) == 4:
        added_time = datetime.timedelta(hours=int(duration[:1]), minutes=int(duration[-2:]))
    else:
        added_time = datetime.timedelta(hours=int(duration[:2]), minutes=int(duration[-2:]))

    # return new_time

add_time("11:06 PM", "2:02")