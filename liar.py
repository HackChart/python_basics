# Now I want you to make a subclass of list. Name it Liar.
# Override the __len__ method so that it always returns the wrong number of items in the list.
# For example, if a list has 5 members, the Liar class might say it has 8 or 2.
# You'll probably need super() for this.
import random


class Liar(list):
    def __len__(self):
        wrong_number = random.randint(0, 10)
        while True:
            if super(Liar, self).__len__() == wrong_number:
                continue
            else:
                return wrong_number


x = Liar([1, 2, 3])
print(len(x))


