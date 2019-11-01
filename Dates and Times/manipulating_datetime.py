import datetime


def minutes(datetime1, datetime2):
    diff = datetime2 - datetime1
    return round(diff.total_seconds() / 60)
