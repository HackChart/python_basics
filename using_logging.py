import logging

# You create a log file, and send alerts to it by using the log library
# This creates a logger file called basic.log, and tells it only to record debug level events
# There are 6 logging levels
# Notset, debug, info, warning, error, and critical
logging.basicConfig(filename= "basic.log", level= DEBUG)
logging.debug("This is a message that will show up under the debug level")
