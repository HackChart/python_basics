import datetime


# Examples
# to_string(datetime_object) => "24 September 2012"
# Create a function that takes a datetime and returns a string
# Use strftime
def to_string(datetime):
    return datetime.strftime(%d %B %Y)

# from_string("09/24/12 18:30", "%m/%d/%y %H:%M") => datetime
