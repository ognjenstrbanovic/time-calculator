# dependencies
import datetime
from datetime import timedelta

def add_time(start, duration, weekday = False):

    # reformatting 'start'; w/ help from GeeksforGeeks...
    typical_start_length = 8
    if start[-2:] == "AM" and start[:2] == "12":
        new_start = "00" + start[2:-2]
    elif start[-2:] == "AM":
        new_start = start[:-2]
    elif start[-2:] == "PM" and start[:2] == "12":
        new_start = start[:-2]
    elif len(start) == typical_start_length:
        new_start = str(int(start[:2]) + 12) + start[2:5]
    else:
        new_start = str(int(start[:1]) + 12) + start[2:5]

    if len(start) == typical_start_length:
        start_time = datetime.datetime.now().replace(hour=int(new_start[:2]), minute=int(new_start[3:]), second=0, microsecond=0)
    else:
        start_time = datetime.datetime.now().replace(hour=int(new_start[:1]), minute=int(new_start[2:]), second=0, microsecond=0)

    if len(duration) == 4:
        if duration[0] != "0":
            added_time = datetime.timedelta(hours=int(duration[0]), minutes=int(duration[-2:]))
        else:
            added_time = datetime.timedelta(minutes=int(duration[-2:]))
    else:
        added_time = datetime.timedelta(hours=int(duration[:2]), minutes=int(duration[-2:]))

    datetime_new_time = start_time + added_time

    # using strftime() method...
    new_time = datetime_new_time.strftime("%-I:%M %p")

    print(datetime_new_time - added_time)

    # logic...
    hours_minutes_seconds_length = 7
    if len(str(datetime_new_time)) == hours_minutes_seconds_length:
        return new_time

print(add_time("11:59 PM", "20:05"))