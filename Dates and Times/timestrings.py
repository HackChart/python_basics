# Create a function named to_string that takes a datetime and gives back a string in the format "24 September 2012".

import datetime

def to_string(date_time):
    return date_time.strftime("%d %B %Y")

# Create a new function named from_string that takes two arguments: a date as a string and an strftime-compatible format string, and returns a datetime created from them.

def from_string(date, date_format: str):
    return datetime.datetime.strptime(date, date_format)