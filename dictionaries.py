# Dictionaries consist of key value pairs that are defined within {}
dictionary = {"key": "value", "name": "Austin", "age": "24", "course": "Beginning Python", }

# Prints the entire contents of the dictionary
print(dictionary)
# Prints the contents of the dictionary as corresponding pairs
print(dictionary.items())
# Prints only the keys in the dictionary
print(dictionary.keys())
# Prints only the values in the dictionary
print(dictionary.values())

# +++++++++++++++++++++++++++++++++++++++
# Iterating over dictionaries
# +++++++++++++++++++++++++++++++++++++++

# Will only print the keys found in the dictionary
for item in dictionary:
    print(item)

# To get the key value pairs, you have to pass in another localized constant
for key, value in dictionary.items():
    print("{}: {}".format(key, value))

# To iterate over specific elements in the dictionary, we can use the methods we used earlier
for key in dictionary.keys():
    print(key)

for value in dictionary.values():
    print(value)

# +++++++++++++++++++++++++++++++++++++++
# Packing with dictionaries
# +++++++++++++++++++++++++++++++++++++++

# Standard packing uses *args to pack variables passed to it into a tuple
def user_information(*args):
    for info in args:
        print(info)


user_information(1, 2, 4, "Austin")


# We can do the same thing using **kwargs, which allows us to pack into a dictionary
def kw_user_information(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


# When we call the function, we can pass variable assignments to it, which are packed into a dictionary called kwargs
kw_user_information(name="Austin", age="24", language="Python")