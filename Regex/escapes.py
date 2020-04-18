# Write a function named first_number that takes a string as an argument. 
# The function should search, with a regular expression, the first number in the string and return the match object.

import re

def first_number(target_string: str):
    return re.search(r'\d', target_string)

# Now, write a function named numbers() that takes two arguments: a count as an integer and a string. Return an re.search for exactly count numbers in the string. Remember, you can multiply strings and integers to create your pattern.


# For example: r"\w" * 5 would create r"\w\w\w\w\w".

def numbers(count: int, target_string: str):
    return re.search(r'\d' * count, target_string)