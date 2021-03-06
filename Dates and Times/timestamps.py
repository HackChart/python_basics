# Create a function named timestamp_oldest that takes any number of POSIX timestamp arguments. Return the oldest one as a datetime object. 
# Remember, POSIX timestamps are floats and lists have a .sort() method.
import datetime

def timestamp_oldest(*args):
    timestamps = []
    for arg in args:
        timestamps.append(arg)
    timestamps.sort()
    return datetime.datetime.fromtimestamp(timestamps[0])
