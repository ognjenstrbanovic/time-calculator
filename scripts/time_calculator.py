# dependencies
import datetime
from datetime import timedelta
import calendar

def add_time(start, duration, weekday = False):


    # reformatting 'start'; w/ help from GeeksforGeeks...
    if start[-2:] == "AM" and start[:2] == "12":
        new_start = "00" + start[2:-3]
    elif start[-2:] == "AM" and (start[:2] == "10" or start[:2] == "11"):
        new_start = str(int(start[:2])) + start[3:5]
    elif start[-2:] == "PM" and (start[:2] == "10" or start[:2] == "11"):
        new_start = str(int(start[:2]) + 12) + start[3:5]
    elif start[-2:] == "AM":
        new_start = "0" + str(int(start[:1])) + start[2:4]
    elif start[-2:] == "PM" and start[:2] == "12":
        new_start = start[:-3]
    else:
        new_start = str(int(start[:1]) + 12) + start[2:4]

    # date=birthday...
    all_weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    if weekday:
        if weekday.title() == all_weekdays[0]:
            start_time = datetime.datetime(year=2020, month=1, day=27, hour=int(new_start[:2]), minute=int(new_start[2:]))
        elif weekday.title() == all_weekdays[1]:
            start_time = datetime.datetime(year=2020, month=1, day=28, hour=int(new_start[:2]), minute=int(new_start[2:]))
        elif weekday.title() == all_weekdays[2]:
            start_time = datetime.datetime(year=2020, month=1, day=29, hour=int(new_start[:2]), minute=int(new_start[2:]))
        elif weekday.title() == all_weekdays[3]:
            start_time = datetime.datetime(year=2020, month=1, day=30, hour=int(new_start[:2]), minute=int(new_start[2:]))
        elif weekday.title() == all_weekdays[4]:
            start_time = datetime.datetime(year=2020, month=1, day=31, hour=int(new_start[:2]), minute=int(new_start[2:]))
        elif weekday.title() == all_weekdays[5]:
            start_time = datetime.datetime(year=2020, month=2, day=1, hour=int(new_start[:2]), minute=int(new_start[2:]))
        elif weekday.title() == all_weekdays[6]:
            start_time = datetime.datetime(year=2020, month=2, day=2, hour=int(new_start[:2]), minute=int(new_start[2:]))
    else:
        start_time = datetime.datetime(year=2020, month=2, day=2, hour=int(new_start[:2]), minute=int(new_start[2:]))

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

    new_time_in_datetime = start_time + added_time

    # using strftime() method...
    new_time = new_time_in_datetime.strftime("%-I:%M %p")

    difference_in_days = new_time_in_datetime.date() - start_time.date()

    # logic for output
    if weekday == False:
        if str(difference_in_days) == "0:00:00":
            return new_time
        elif str(difference_in_days)[:2] == "1" + " ":
            new_time += " (next day)"
            return new_time
        elif str(difference_in_days)[:2] != "1" + " ":
            if str(difference_in_days)[1] == " ":
                new_time += f" ({str(difference_in_days)[0]} days later)"
                return new_time
            else:
                new_time += f" ({str(difference_in_days)[:2]} days later)"
            return new_time
    else:
        if str(difference_in_days) == "0:00:00":
            return f"{new_time}, {all_weekdays[new_time_in_datetime.weekday()]}"
        elif str(difference_in_days)[:2] == "1" + " ":
            new_time += f", {all_weekdays[new_time_in_datetime.weekday()]} (next day)"
            return new_time
        if str(difference_in_days)[1] == " ":
            new_time += f", {all_weekdays[new_time_in_datetime.weekday()]} ({str(difference_in_days)[:1]} days later)"
            return new_time
        else:
            new_time += f", {all_weekdays[new_time_in_datetime.weekday()]} ({str(difference_in_days)[:2]} days later)"
            return new_time