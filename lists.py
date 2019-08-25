import sys

shopping_list = []


def add_item(item):
    item = item.title()
    shopping_list.append(item)
    print("There are now {} items on the list.".format(len(shopping_list)))


def help_menu():
    print("""
    HELP:

    ----------------------------------------------------------------------------------------------

    > TO ADD AN ITEM TO THE LIST: Type the name of the item you would like to add and press enter.
    > TO VIEW YOUR CURRENT LIST: Type VIEWLIST into the console and press enter
    (List can be edited and verified while viewing)
    > TO COMPLETE YOUR LIST: Type DONE into the console.
    """)


def view_list():
    item_number = 1
    for item in shopping_list:
        print("{}: {}".format(item_number, item))
        item_number += 1


def done():
    print("\nHere is your list:\n----------------------------")
    view_list()
    sys.exit("")


# TODO: Add access to help menu
def verify_order():
    while True:
        is_correct = input("Does this look right?\nY/N  ")
        if is_correct.lower() == "y":
            print("Great!")
            done()
        elif is_correct.lower() == "n":
            print("Okay, what would you like to change?")
            print("You can enter REMOVE to erase an item from the list, REPLACE to change one, or FINISH to go back\n"
                  "to adding items.")
            # TODO: Create error handling for int input and non keyword values
            while True:
                will_change = input("What would you like to do? ")
                if will_change.lower() == "remove":
                    view_list()
                    remove_item = int(input("Please enter the number of the item that you would like to remove:   "))
                    del shopping_list[remove_item - 1]
                    view_list()
                    continue
                elif will_change.lower() == "replace":
                    view_list()
                    replace_num = int(input("Please enter the number of the item that you would like to replace    "))
                    replacement_item = input("What you would like to change this to?    ")
                    shopping_list[replace_num - 1] = replacement_item.title()
                    view_list()
                    continue
                elif will_change.lower() == "finish":
                    view_list()
                    break
        # TODO: Create a better way to get back to adding items
        elif is_correct.lower() == "finish":
            break
        else:
            print("Please enter Y/N")
            continue


# Welcome the user to the program/explain help
print("""
    Welcome to Lists!
    -------------------------------------------------------------
    Here, you can create a list of whatever your heart desires!
    If at any time, you need help, just type HELP into the console. 
    """)


# Loop that will constantly ask the user if they want to add a new item until they are done
while True:
    new_item = input("What would you like to add?   ")
    if new_item.lower() == "viewlist":
        view_list()
        verify_order()
        continue
    elif new_item.lower() == "done":
        done()
    elif new_item.lower() == "help":
        help_menu()
        continue
    else:
        add_item(new_item)






