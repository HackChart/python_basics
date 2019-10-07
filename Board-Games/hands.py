from dice import D20


class Hand(list):
    def __init__(self, constructor=None):
        super().__init__()
        for item in constructor:
            self.append(item)


    @property
    def total(self):
        return sum(self)

    @classmethod
    def roll(cls, quantity):
        constructor = []
        for _ in range(quantity):
            constructor.append(D20())
        return cls(constructor)


if __name__ == "__main__":
    hand = Hand.roll(2)
    print(hand)
    print(hand.total)