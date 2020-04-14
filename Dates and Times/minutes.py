# Write a function named minutes that takes two datetimes and, using timedelta.total_seconds() to get the number of seconds, returns the number of minutes, rounded, between them. 
# The first will always be older and the second newer. You'll need to subtract the first from the second.

import datetime

def minutes(datetime_a, datetime_b):
    diff = datetime_b - datetime_a
    return round(diff.total_seconds() / 60)