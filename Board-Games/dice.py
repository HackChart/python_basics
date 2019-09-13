import random


class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("You cannot have a die with less than 2 sides")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")
        self.value = value or range(1, sides)


class D6(Die):
    def __init__(self, value):
        super().__init__(sides=6, value=value)



