import random


class Die:
    def __init__(self, sides=2):
        if not sides >= 2:
            raise ValueError("You cannot have a die with less than 2 sides")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        self.value = random.randint(1, sides)

    def __int__(self):
        return int(self.value)

    def __eq__(self, other):
        return int(self) == other

    def __lt__(self, other):
        return int(self) < other

    def __gt__(self, other):
        return int(self) > other

    def __ge__(self, other):
        return int(self) > other or int(self) == other

    def __le__(self, other):
        return int(self) < other or int(self) == other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)


class D6(Die):
    def __init__(self):
        super().__init__(sides=6)


class D20(Die):
    def __init__(self):
        super(D20, self).__init__(sides=20)



