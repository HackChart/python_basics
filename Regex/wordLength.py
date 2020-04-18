# Create a function named find_words that takes a count and a string. Return a list of all of the words in the string that are count word characters long or longer.

import re

def find_words(count: int, target: str):

    return re.findall(rf'\w{{{count},}}', target)

if __name__ == '__main__':
    print(find_words(4, "dog, cat, whale"))