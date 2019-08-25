
# ++++++++++++++++++++++++++++++++++++++++++
# SEQUENCE OPERATIONS COMMON TO ALL ALL TYPES
# +++++++++++++++++++++++++++++++++++++++++

# ==========================================
# CONCATNATION
# ==========================================
# Attachs one sequence to the end of another

nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [7, 8, 9, 10]
combined_nums = nums1 + nums2

# ==========================================
# MULTIPLICATION
# ==========================================
# Adds the sequence to itself a specified number of times

student_gpas = [2.0, 3.1, 4.0, 2.3, 3.3, 3.1]
student_gpas * 2  # [2.0, 3.1, 4.0, 2.3, 3.3, 3.1, 2.0, 3.1, 4.0, 2.3, 3.3, 3.1]

# ==========================================
# COUNT
# ==========================================
# Returns the number of times an arguement appears in a sequence

student_gpas = [2.0, 3.1, 4.0, 2.3, 3.3, 3.1]
student_gpas.count(3.1)  # Shows up 2 times

# ==========================================
# IN
# ==========================================
# Returns a boolean of whether or not an arguement is contained in a sequence

student_gpas = [2.0, 3.1, 4.0, 2.3, 3.3, 3.1]
2.0 in student_gpas  # True

# ==========================================
# INDEX
# ==========================================
# Returns the index position of the first time that an argument appears

student_gpas = [2.0, 3.1, 4.0, 2.3, 3.3, 3.1]
student_gpas.index(3.1)  # 1

# ==========================================
# LEN
# ==========================================
# Returns the number of items in a sequence

student_gpas = [2.0, 3.1, 4.0, 2.3, 3.3, 3.1]
len(student_gpas)  # 6

# ==========================================
# MAX
# ==========================================
# Returns the max value in a sequence

student_gpas = [2.0, 3.1, 4.0, 2.3, 3.3, 3.1]
max(student_gpas)  # 4.0

# ==========================================
# MIN
# ==========================================
# Returns the lowest value in a sequence

student_gpas = [2.0, 3.1, 4.0, 2.3, 3.3, 3.1]
min(student_gpas)  # 2.0

# ==========================================
# SLICING
# ==========================================
# Returns a specified portion of a sequence
# slice[start:stop:step]

grocery_list = ["tomato", "cheese", "buns", "meat", "lettuce"]
print(grocery_list[:2])

# slices can go all the way to the end of a list if you leave out stop value
print(grocery_list[2:])

# skip every other item in the list by changing step value
print(grocery_list[::2])

# reverses the order of the list. DOES NOT CHANGE ACTUAL ORDER OF LIST
print(grocery_list[::-1])

# ++++++++++++++++++++++++++++++++++++++++++
# MUTABLE SEQUENCE ONLY OPERATIONS
# ++++++++++++++++++++++++++++++++++++++++++

# ==========================================
# APPEND
# ==========================================
# Adds a value onto the end of a list

my_pets = ['Scofield', 'Edel', 'Ernie', 'Squash']

my_pets.append('Vera') # ['Scofield', 'Edel', 'Ernie', 'Squash', 'Vera']

# ==========================================
# DEL
# ==========================================
# Deletes a slice from a sequence

my_pets = ['Scofield', 'Edel', 'Ernie', 'Squash', 'Vera']

del my_pets[0:2] # ['Ernie', 'Squash', 'Vera']

# ==========================================
# INSERT
# ==========================================
# Adds an item to the list at a specified index

fruits = ['apple', 'banana', 'orange', 'pear', 'strawberry']

fruits.insert(2, 'kiwi') # ['apple', 'banana', 'kiwi', 'orange', 'pear', 'strawberry']

# ==========================================
# POP
# ==========================================
# Removes item from a sequence, but also retrieves it

fruits = ['apple', 'banana', 'orange', 'pear', 'strawberry']

apple = fruits.pop(0) # ['banana', 'orange', 'pear', 'strawberry'], apple = 'apple'

# ==========================================
# REMOVE
# ==========================================
# Removes the first ocurrence of an argument from a sequence

student_gpas = [2.5, 4.0, 3.2, 2.9, 3.7, 1.5, 4.0]

student_gpas.remove(4.0) # [2.5, 3.2, 2.9, 3.7, 1.5, 4.0]

# ==========================================
# REVERSE
# ==========================================
# Reverses sequence in place

my_pets = ['Ernie', 'Squash', 'Vera']

my_pets.reverse() # ['Vera', 'Squash', 'Ernie']










