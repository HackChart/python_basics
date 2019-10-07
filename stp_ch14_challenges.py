
class Square:
    square_list = []

    def __init__(self, side_length):
        self.side_length = side_length
        self.square_list.append(self)

    def __repr__(self):
        return "The length of each side of this square is {}".format(self.side_length)


def compare_objects(obj1, obj2):
    return obj1 is obj2


if __name__ == "__main__":
    s1 = Square(1)
    s2 = Square(2)
    print(s1.square_list)
