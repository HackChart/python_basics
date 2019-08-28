# Now I want you to make a subclass of list. Name it Liar.
# Override the __len__ method so that it always returns the wrong number of items in the list.
# For example, if a list has 5 members, the Liar class might say it has 8 or 2.
# You'll probably need super() for this.
import random


class Liar(list):
    # TODO: Find out why we override len since it isnt a method
    def __len__(self):
        return len(self)


x = Liar([1, 2, 3, 4])
print(len(x))