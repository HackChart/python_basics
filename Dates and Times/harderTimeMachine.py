# Write a function named time_machine that takes an integer and a string of "minutes", "hours", "days", or "years". 
# This describes a timedelta. Return a datetime that is the timedelta's duration from the starter datetime.

import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

def time_machine(i: int, classifier: str) -> datetime.datetime:
    if classifier == "years":
        duration = datetime.timedelta(days=(i * 365))
    elif classifier == "days":
        duration = datetime.timedelta(days=i)
    elif classifier == "hours":
        duration = datetime.timedelta(hours=i)
    else:
        duration = datetime.timedelta(minutes=i)
    return starter + duration
# Remember, you can't set "years" on a timedelta!
# Consider a year to be 365 days.

## Example
# time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)

