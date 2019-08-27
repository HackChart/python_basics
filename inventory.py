class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)


class SortedInventory(Inventory):
    def add_item(self, item):  # By creating our own add_item method, we can override the one found in the parent
        super().add_item(item)  # Calling super() allows you to access a method from the parent
        # This allows us to keep the functionality of the original method, while adding on to it in the child
        self.slots.sort()  # Sorts the list 
