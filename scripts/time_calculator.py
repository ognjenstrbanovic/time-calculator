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

    start_time = datetime.datetime.now().replace(hour=int(new_start[:2]), minute=int(new_start[3:]), second=0, microsecond=0)

    if len(duration) == 4:
        if duration[0] != "0":
            added_time = datetime.timedelta(hours=int(duration[0]), minutes=int(duration[-2:]))
        else:
            added_time = datetime.timedelta(minutes=int(duration[-2:]))
    else:
        added_time = datetime.timedelta(hours=int(duration[:2]), minutes=int(duration[-2:]))

    unformatted_new_time = start_time + added_time

    # using strftime() method...
    new_time = unformatted_new_time.strftime("%I:%M %p")

    # logic...
    hour_minute_second_length = 7
    if len(str(unformatted_new_time - start_time)) > 7 and weekday == True:
        if str(unformatted_new_time - start_time)[0] == "1" and str(unformatted_new_time - start_time)[1] == " ":
            new_time += " (next day)"
            return new_time
        elif str(unformatted_new_time - start_time)[4] == "y":
            new_time += str(unformatted_new_time - start_time)[:5]
            return new_time
        else:
            new_time += str(unformatted_new_time - start_time)[:6]
            return new_time
    else:
        return new_time

print(add_time("11:40 AM", "31:25"))