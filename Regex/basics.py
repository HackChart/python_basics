import re

with open("basics.txt") as file_object:
    data = file_object.read()
    
first = re.match(r'Four', data) # Use match to find patterns at the beginning of a string
liberty = re.search(r'Liberty', data) # Use search to find patterns anywhere within a string