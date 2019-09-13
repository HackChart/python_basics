# Create a class called shape with a method called what_i_am
class Shape:
    def what_i_am(self):
        print("I am a shape")


# Create rectangle and square classes with a method that calculates area and returns it
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    @property
    def perimeter(self):
        return self.side_length * 4

    # Define a method in Square called change_size that allows you to increment or decrement the sides
    def change_size(self):
        new_side_length = input("What would you like to change the length of the side by?  ")
        self.side_length += int(new_side_length)
        print("The length of the side has been changed to {}".format(self.side_length))


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def perimeter(self):
        return (self.length * 2) + (self.width * 2)


# Create a class called Horse and Rider. Use composition to model a horse that has a rider
class Rider:
    def __init__(self, name):
        self.name = name


class Horse:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner


if __name__ == "__main__":
    square = Square(5)
    rectangle = Rectangle(4, 3)
    print("The perimeter of the square is {}".format(square.perimeter))
    square.change_size()
    square.what_i_am()
    print("The perimeter of the rectangle is {}".format(rectangle.perimeter))
    rectangle.what_i_am()
    rider = Rider("Austin")
    horse = Horse("Boo", rider)
    print(horse.owner.name)

