# Create a variable named moscow that holds a datetime.timezone object at +4 hours.
import datetime

moscow = datetime.timezone(datetime.timedelta(hours=4))

# Now create a timezone variable named pacific that holds a timezone at UTC-08:00.
pacific = datetime.timezone(datetime.timedelta(hours=-8))

# Finally, make a third variable named india that hold's a timezone at UTC+05:30.
india = datetime.timezone(datetime.timedelta(hours=5, minutes=30))