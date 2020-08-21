# dependencies
import datetime
def add_time(start, duration, weekday = False):

    if "AM" in start:
        AM_start_cleaned = start.strip(" AM").split(":")
    elif "PM" in start:
        PM_start_cleaned = start.strip(" PM").split(":")



    return PM_start_cleaned
    # return new_time

add_time("11:06 PM", "2:02")