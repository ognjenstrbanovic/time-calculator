# dependencies
import datetime
from datetime import timedelta

def add_time(start, duration, weekday = False):


    # reformatting 'start'; w/ help from GeeksforGeeks...
    if start[-2:] == "AM" and start[:2] == "12":
        new_start = "00" + start[2:-3]
    elif start[:2] == "10" or start[:2] == "11":
        new_start = str(int(start[:2]) + 12) + start[3:5]
    elif start[-2:] == "AM":
        new_start = "0" + str(int(start[:1])) + start[2:4]
    elif start[-2:] == "PM" and start[:2] == "12":
        new_start = start[:-3]
    else:
        new_start = str(int(start[:1]) + 12) + start[2:4]

    print(new_start)

    start_time = datetime.datetime.now().replace(hour=int(new_start[:2]), minute=int(new_start[2:]), second=0, microsecond=0)

    # print(start_time)

    # reformatting added_time...
    if len(duration) == 4:
        if duration[0] != "0":
            added_time = datetime.timedelta(hours=int(duration[0]), minutes=int(duration[-2:]))
        else:
            added_time = datetime.timedelta(minutes=int(duration[-2:]))
    elif len(duration) == 5:
        added_time = datetime.timedelta(hours=int(duration[:2]), minutes=int(duration[-2:]))
    elif len(duration) == 6:
        added_time = datetime.timedelta(hours=int(duration[:3]), minutes=int(duration[-2:]))
    else:
        added_time = datetime.timedelta(hours=int(duration[:1]), minutes=int(duration[-2:]))

    # print(added_time)

    datetime_new_time = start_time + added_time

    # print(datetime_new_time)

    # using strftime() method...
    new_time = datetime_new_time.strftime("%-I:%M %p")

    # logic...
    difference_in_days = datetime_new_time.date() - start_time.date()

    # print(difference_in_days)

    if str(difference_in_days) == "0:00:00":
        return new_time
    elif str(difference_in_days)[:2] == "1" + " ":
        new_time += " (next day)"
        return new_time
    elif str(difference_in_days)[:2] != "1" + " ":
        if str(difference_in_days)[1] == " ":
            new_time += f" ({str(difference_in_days)[0]} days later)"
        else:
            new_time += f" ({str(difference_in_days)[:2]} days later)"
        return new_time


print(add_time("8:16 PM", "466:02"))