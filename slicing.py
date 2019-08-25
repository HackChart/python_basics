# slice[start:stop:step]

grocery_list = ["tomato", "cheese", "buns", "meat", "lettuce"]
print(grocery_list[:2])

# slices can go all the way to the end of a list if you leave out stop value
print(grocery_list[2:])

# skip every other item in the list by changing step value
print(grocery_list[::2])

# reverses the order of the list. DOES NOT CHANGE ACTUAL ORDER OF LIST
print(grocery_list[::-1])
