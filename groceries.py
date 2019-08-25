groceries = ['roast beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food']

# Iterates through every item in the list and prints it individually
for item in groceries:
    print(item)

# Creates an index number that is formatted with each item that is printed
index = 1
for item in groceries:
    print(f'{index}: {item}')
    index += 1

# Uses enumerate() to format that index value of each item in the list
# index, item is a declared tuple of both values we intend to format
# groceries is the list we want to interate over
# 1 is the number that we want enum to start at (otherwise it starts at 0)
for index, item in enumerate(groceries, 1):
    print(f'{index}: {item}')
