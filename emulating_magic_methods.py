class Inventory:
    def __init__(self):
        self.slots = []  # Initializes the slots attribute on new instance

    def add_item(self, item):
        self.slots.append(item)

    def __len__(self):  # Overrides len to determine number of items in inventory
        return len(self.slots)

    def __contains__(self, item):  # Overrides contains to determine if an item is in inventory
        return item in self.slots
