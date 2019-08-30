# Alright, here's a fun task!
# Create a function named combiner that takes a single argument, which will be a list made up of strings and numbers.
# Return a single string that is a combination of all of the strings in the list and then the sum of all of the numbers.
# For example, with the input ["apple", 5.2, "dog", 8], combiner would return "appledog13.2".
# Be sure to use isinstance to solve this as I might try to trick you.


def combiner(*args):
    strings = []
    nums = []

    for arg in args:
        # TODO: Refactor elif statements
        if isinstance(arg, list):
            for item in arg:
                if isinstance(item, str):
                    strings.append(item)
                elif isinstance(item, (int, float)):
                    nums.append(item)
                else:
                    print("The value was not added")
        elif isinstance(arg, str):
            strings.append(arg)
        elif isinstance(arg, (int, float)):
            nums.append(arg)
        else:
            print("The value was not added")

    combined_string = "".join(strings)
    sum_of_nums = sum(nums)
    all_combined = "{}{}".format(combined_string, sum_of_nums)
    print(all_combined)


test_list = ["apple", 5.2, "dog", 8]
combiner(test_list, "Harley", "Nala", "Boo", 3)
