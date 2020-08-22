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
    start_time = datetime.datetime.now().replace(month=2, day=2, hour=int(new_start[:2]), minute=int(new_start[2:]), second=0, microsecond=0)

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

    weekdays_dictionary = dict(enumerate(calendar.day_name))
    if weekday.title() == list(weekdays_dictionary.keys())[0]:
        calendar.setfirstweekday(calendar.MONDAY)
    elif weekday.title() == list(weekdays_dictionary.keys())[1]:
        calendar.setfirstweekday(calendar.TUESDAY)
    elif weekday.title() == list(weekdays_dictionary.keys())[2]:
        calendar.setfirstweekday(calendar.WEDNESDAY)
    elif weekday.title() == list(weekdays_dictionary.keys())[3]:
        calendar.setfirstweekday(calendar.THURSDAY)
    elif weekday.title() == list(weekdays_dictionary.keys())[4]:
        calendar.setfirstweekday(calendar.FRIDAY)
    elif weekday.title() == list(weekdays_dictionary.keys())[5]:
        calendar.setfirstweekday(calendar.SATURDAY)
    elif weekday.title() == list(weekdays_dictionary.keys())[6]:
        calendar.setfirstweekday(calendar.SUNDAY)
    print(calendar.setfirstweekday(calendar.MONDAY))
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
            return f"{new_time}, {current_weekday}"
        elif str(difference_in_days)[:2] == "1" + " ":
            new_time += f", {current_weekday} (next day)"
            return new_time
        if str(difference_in_days)[1] == " ":
            new_time += f", {current_weekday} ({str(difference_in_days)[:1]} days later)"
            return new_time
        else:
            new_time += f", {current_weekday} ({str(difference_in_days)[:2]} days later)"
            return new_time


print(add_time("2:59 AM", "24:00", "Monday"))