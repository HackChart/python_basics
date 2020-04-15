# Create a function named to_timezone that takes a timezone name as a string. Convert starter to that timezone using pytz's timezones and return the new datetime.

import datetime
import pytz


starter = pytz.utc.localize(datetime.datetime(2015, 10, 21, 23, 29))

def to_timezone(tz_name: str):
    return starter.astimezone(pytz.timezone(tz_name))
