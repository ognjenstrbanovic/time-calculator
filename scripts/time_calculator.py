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

    print(new_start)

    if len(start) == typical_start_length:
        start_time = datetime.datetime.now().replace(hour=int(new_start[:2]), minute=int(new_start[3:]), second=0, microsecond=0)
    else:
        if len(new_start) == 4 and new_start[0] == "0":
            start_time = datetime.datetime.now().replace(hour=int(new_start[:1]), minute=int(new_start[2:]), second=0, microsecond=0)
        elif len(new_start) == 4 and new_start[0] != "0":
            start_time = datetime.datetime.now().replace(hour=int(new_start[:2]), minute=int(new_start[2:]), second=0, microsecond=0)

    print(start_time)
    
    # reformatting added_time...
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

    # logic...
    hour_minute_second_length = 7
    if len(str(datetime_new_time - start_time)) == 7:
        return new_time
    elif str(datetime_new_time.date() - start_time.date())[:2] == "0:00:00":
        return new_time
    elif str(datetime_new_time.date() - start_time.date())[:2] == "1" + " ":
        new_time += " (next day)"
        return new_time
    elif str(datetime_new_time.date() - start_time.date())[0] != "1" + " ":
        if str(datetime_new_time.date() - start_time.date())[1] == " ":
            new_time += f" ({str(datetime_new_time.date() - start_time.date())[0]} days later)"
        else:
            new_time += f" ({str(datetime_new_time.date() - start_time.date())[:2]} days later)"
        return new_time

print(add_time("5:01 AM", "0:00"))