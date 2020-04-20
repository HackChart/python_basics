# Create a function named find_emails that takes a string. Return a list of all of the email addresses in the string.
# # Example:
# >>> find_email("kenneth.love@teamtreehouse.com, @support, ryan@teamtreehouse.com, test+case@example.co.uk")
# ['kenneth@teamtreehouse.com', 'ryan@teamtreehouse.com', 'test@example.co.uk']

import re

def find_emails(target: str):
    return re.findall(r'[-\w\d+.]+@[-\w\d.]+', target, re.I)