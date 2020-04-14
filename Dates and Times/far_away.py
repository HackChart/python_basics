# Write a function called far_away that takes one argument, a timedelta. Add that timedelta to datetime.datetime.now() and return the resulting datetime object.

import datetime

def far_away(timedelta):
    return datetime.datetime.now() + timedelta